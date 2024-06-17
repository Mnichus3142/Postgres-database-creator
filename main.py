import os
import time
import components.gk as gk
import json
import components.passwordHider as passwordHider
import psycopg2

art = """
  ____  ____   ___  _       ____  ____     ____                _             
 |  _ \/ ___| / _ \| |     |  _ \| __ )   / ___|_ __ ___  __ _| |_ ___  _ __ 
 | |_) \___ \| | | | |     | | | |  _ \  | |   | '__/ _ \/ _` | __/ _ \| '__|
 |  __/ ___) | |_| | |___  | |_| | |_) | | |___| | |  __/ (_| | || (_) | |   
 |_|   |____/ \__\_\_____| |____/|____/   \____|_|  \___|\__,_|\__\___/|_|   
                                                                             
"""

conn = 0

connection_parameters = {
    "host": '',
    "port": 5432,
    "user": '',
    "password": ''
}

class query:
    line = 0
    queryToReturn = ""
    
    def __init__(self, tableName) -> None:
        self.queryToReturn = "CREATE TABLE " + tableName + " ("
        
    def addColumn (self, columnName, tab) -> None:
        if self.line == 0:
            self.queryToReturn = self.queryToReturn + columnName + " " + tab[0]
            if tab[1] != '0':
                self.queryToReturn = self.queryToReturn + "(" + tab[1] + ")"
            if tab[2] != "False":
                self.queryToReturn = self.queryToReturn + " NOT NULL"
            if tab[3] != "False":
                self.queryToReturn = self.queryToReturn + " UNIQUE"
            if tab[4] != "False":
                self.queryToReturn = self.queryToReturn + " PRIMARY KEY"
            self.line = 1
        
        else:
            self.queryToReturn = self.queryToReturn + ", "
            self.queryToReturn = self.queryToReturn + columnName + " " + tab[0]
            if tab[1] != '0':
                self.queryToReturn = self.queryToReturn + "(" + tab[1] + ")"
            if tab[2] != "False":
                self.queryToReturn = self.queryToReturn + " NOT NULL"
            if tab[3] != "False":
                self.queryToReturn = self.queryToReturn + " UNIQUE"
            if tab[4] != "False":
                self.queryToReturn = self.queryToReturn + " PRIMARY KEY"
    
    def endQuery(self) -> None:
        self.queryToReturn = self.queryToReturn + ");"
    
    def returnQuery(self) -> str:
        return self.queryToReturn

def cleaner ():
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(art)
        
def createDatabase ():  
    global conn
    global connection_parameters
    
    with open('setup.json', 'r') as setup:
        setup_data = json.load(setup)
    
    databaseName = setup_data['databaseName'].lower()
    print(databaseName)
    
    # *Creating database
    
    cursor = conn.cursor()
    cursor.execute("SELECT datname FROM pg_database")
    conn.commit()
    cur = cursor.fetchall()
    tab = [str(x)[2:-3] for x in cur]
    
    # *If database doesn't exists
    
    if databaseName not in tab:
        try:
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE {databaseName}")
            cleaner()
        except:
            cleaner()
            print("Error code 1")
            time.sleep(3)
            return 0
        
    # *If database extist
        
    else:        
        menuElements = ["Yes", "No"]
        currentPos = 0
        menu = True
        
        while menu:
            cleaner()
            print("Database already created\nDo you want to drop it and create new?\n")
            
            for i in range(len(menuElements)):
                if i == currentPos:
                    print(f"-> {menuElements[i]}")
                else:
                    print(menuElements[i])
                    
            button = gk.getkeyInASCII()
            
            # Move logic
            
            if button == 72 and currentPos != 0:
                currentPos -= 1
            
            elif button == 80 and currentPos != len(menuElements) - 1:
                currentPos += 1
                
            # What every button should do
                
            if (button == 13 or button == 10) and currentPos == 0:
                conn.autocommit = True
                cursor.execute(f"DROP DATABASE {databaseName}")
                cursor.execute(f"CREATE DATABASE {databaseName}")
                menu = False
                
            elif (button == 13 or button == 10) and currentPos == len(menuElements) - 1:
                cleaner()
                print("Goodbye")
                time.sleep(1)
                exit()
                
    cursor.close()
    conn.close()  

    conn = psycopg2.connect(
        host = connection_parameters["host"],
        port = connection_parameters["port"],
        user = connection_parameters["user"],
        password = connection_parameters["password"],
        dbname = databaseName
    )
    
    cursor = conn.cursor()
                
    # *Creating admin user
    
    # *If admin do not exist

    if 'databaseAdminName' in setup_data:
        databaseAdminName = setup_data['databaseAdminName'].lower()
        
        cursor.execute("select usename from pg_catalog.pg_user")
        conn.commit()
        cur = cursor.fetchall()
        tab = [str(x)[2:-3] for x in cur]
        
        if databaseAdminName not in tab:
            # *Setting password for database admin
            passwordDoNotMatch = True
            password = ""
            
            while passwordDoNotMatch:
                cleaner()
                print(f"Admin name: {databaseAdminName}\n\nCreating password\n")
                pass1 = passwordHider.passwordHider("Enter new admin password: ")
                print()
                pass2 = passwordHider.passwordHider("Confirm new admin password: ")
                
                if pass1 == pass2:
                    passwordDoNotMatch = False
                    password = pass1
                
                else:
                    print("\n\n Passwords do not match, try again")
                    time.sleep(0.5)
            
            try:
                cursor.execute(f"CREATE USER {databaseAdminName} WITH ENCRYPTED PASSWORD '{password}'")
                
                cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {databaseName} TO {databaseAdminName}")
                cursor.execute(f"GRANT ALL ON SCHEMA public TO {databaseAdminName}")
            except:
                cleaner()
                print("Error code 3")
                time.sleep(3)
                return 0
            
        # *If admin already exist
            
        else:
            cleaner()
            
            menuElements = ["Yes", "No", "Exit setup"]
            currentPos = 0
            menu = True
            
            while menu:
                cleaner()
                print("User already exist\nDo you want to delete it and create a new one?\n")
                
                for i in range(len(menuElements)):
                    if i == currentPos:
                        print(f"-> {menuElements[i]}")
                    else:
                        print(menuElements[i])
                        
                button = gk.getkeyInASCII()
                
                # Move logic
                
                if button == 72 and currentPos != 0:
                    currentPos -= 1
                
                elif button == 80 and currentPos != len(menuElements) - 1:
                    currentPos += 1
                    
                # What every button should do
                    
                if (button == 13 or button == 10) and currentPos == 0:
                    try:
                        cursor.execute(f"REVOKE ALL ON SCHEMA public FROM {databaseAdminName}")
                        cursor.execute(f"REVOKE ALL PRIVILEGES ON DATABASE {databaseName} FROM {databaseAdminName}")
                        cursor.execute(f"DROP USER {databaseAdminName}")
                    except:
                        cleaner()
                        print("Error code 2")
                        time.sleep(3)
                        return 0
                    
                    # *Setting password for database admin
                    passwordDoNotMatch = True
                    password = ""
                    
                    while passwordDoNotMatch:
                        cleaner()
                        print(f"Creating database: {databaseName}\n\nAdmin name: {databaseAdminName}\n\nCreating password\n")
                        pass1 = passwordHider.passwordHider("Enter new admin password: ")
                        print()
                        pass2 = passwordHider.passwordHider("Confirm new admin password: ")
                        
                        if pass1 == pass2:
                            passwordDoNotMatch = False
                            password = pass1
                            
                        else:
                            print("\n\nPasswords do not match, try again")
                            time.sleep(0.5)
                    
                    try:
                        cursor.execute(f"CREATE USER {databaseAdminName} WITH ENCRYPTED PASSWORD '{password}'")
                        cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {databaseName} TO {databaseAdminName}")
                        cursor.execute(f"GRANT ALL ON SCHEMA public TO {databaseAdminName}")
                        menu = False
                    except:
                        cleaner()
                        print("Error code 3")
                        time.sleep(3)
                        return 0
                    
                elif (button == 13 or button == 10) and currentPos == 1:
                    cleaner()
                    print("User not created, processing to next step")
                    menu = False
                    time.sleep(1)
                    
                    
                elif (button == 13 or button == 10) and currentPos == len(menuElements) - 1:
                    cleaner()
                    print("Exiting setup")
                    cursor.execute(f"DROP DATABASE {databaseName}")
                    return 0
    
    # *Creating tables
    
    cleaner()
    print("Creating tables...")
    time.sleep(2)
    
    try:
        for i in setup_data["tabs"]:
            queryToExecute = query(i)
            for j in setup_data["tabs"][i]:
                tab = []
                for x in setup_data["tabs"][i][j]:
                    tab.append(f"{setup_data["tabs"][i][j][x]}")
                queryToExecute.addColumn(j, tab)
            queryToExecute.endQuery();
            conn.autocommit = True
            cursor.execute(queryToExecute.returnQuery())
            conn.commit()
        
    except:
        cleaner()
        print("Error code 4")
        time.sleep(3)
        return 0
        
    conn = psycopg2.connect(
        host = connection_parameters["host"],
        port = connection_parameters["port"],
        user = connection_parameters["user"],
        password = connection_parameters["password"],
    )

def main ():
    global conn
    global connection_parameters
    
    ifEstablished = 0
    
    while ifEstablished == 0:
        cleaner()
        
        connection_parameters["host"] = input("IP address: ")
        connection_parameters["port"] = 5432
        portTemp = input("Port (leave blank for default): ")
        
        if portTemp != '':
            connection_parameters["port"] = portTemp
        
        connection_parameters["user"] = input("Username: ")
        
        connection_parameters["password"] = passwordHider.passwordHider("Password: ")
        
        try:
            conn = psycopg2.connect(
                host = connection_parameters["host"],
                port = connection_parameters["port"],
                user = connection_parameters["user"],
                password = connection_parameters["password"],
            )
            
            ifEstablished = 1
            
        except:
            print("\n\nWrong creditials")
            time.sleep(0.5)
            
    menuElements = ["Create database from json file", "Exit"]
    currentPos = 0
    
    while True:
        cleaner()   
        
        for i in range(len(menuElements)):
            if i == currentPos:
                print(f"-> {menuElements[i]}")
            else:
                print(menuElements[i])
                
        button = gk.getkeyInASCII()
        
        # Move logic
        
        if button == 72 and currentPos != 0:
            currentPos -= 1
        
        elif button == 80 and currentPos != len(menuElements) - 1:
            currentPos += 1
            
        # What every button should do
            
        if (button == 13 or button == 10) and currentPos == 0:
            output = createDatabase()
            if output == 0:
                return 0;
            
        elif (button == 13 or button == 10) and currentPos == len(menuElements) - 1:
            conn.close()
            cleaner()
            print("Goodbye")
            time.sleep(1)
            return 0

if __name__ == "__main__":
    main()