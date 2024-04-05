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

def cleaner ():
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(art)
        
def createDatabase (connection_parameters):  
    global conn
    
    with open('setup.json', 'r') as setup:
        setup_data = json.load(setup)
    
    # *Variables
    
    databaseName = setup_data['databaseName']
    databaseAdminName = setup_data['databaseAdminName']
    groupName = setup_data['databaseName'] + "Users"
    
    # *Creating database
    
    cursor = conn.cursor()
    cursor.execute("SELECT datname FROM pg_database")
    conn.commit()
    cur = cursor.fetchall()
    tab = [str(x)[2:-3] for x in cur]
    
    if databaseName not in tab:
        try:
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE {databaseName}")
            cleaner()
        except:
            cleaner()
            print("Error code 1")
            time.sleep(5)
            return 0
        
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
                cursor = conn.cursor()
                cursor.execute(f"DROP DATABASE {databaseName}")
                cursor.execute(f"CREATE DATABASE {databaseName}")
                menu = False
                
            elif (button == 13 or button == 10) and currentPos == len(menuElements) - 1:
                cleaner()
                print("Goodbye")
                time.sleep(1)
                exit()
    
    # with conn:
    #     with conn.cursor() as cur:
    #         # Creating database
    #         try:
    #             conn.autocommit = True
    #             cur.execute("CREATE DATABASE test")
    #         except:
    #             cleaner()
    #             print("Error code 1")
    #             time.sleep(3)
    #             cur.close()
    #             conn.close()
    #             return 0
    
    # time.sleep(4)
    
    # cur.close()
    # conn.close()
    
    # # Setting password for database admin
    # passwordDoNotMatch = True
    # password = ""
    
    # while passwordDoNotMatch:
    #     cleaner()
    #     print(f"Creating database: {databaseName}\n\nAdmin name: {databaseAdminName}\n\nCreating password\n")
    #     pass1 = passwordHider.passwordHider("Enter new admin password: ")
    #     print()
    #     pass2 = passwordHider.passwordHider("Confirm new admin password: ")
        
    #     if pass1 == pass2:
    #         passwordDoNotMatch = False
    #         password = pass1
            
    # # Creating database group and admin
    
    # try:
    #     cur.execute(sql.SQL("CREATE GROUP {}").format(sql.Identifier(groupName)))
    #     # cur.execute(sql.SQL("CREATE USER {} WITH ENCRYPTED PASSWORD '{}'").format(sql.Identifier(setup_data['databaseAdminName']), sql.Identifier(password)))
    #     # cur.execute(sql.SQL("ALTER GROUP {} ADD USER {}").format(sql.Identifier(f"{setup_data['databaseName']} + users"), sql.Identifier(setup_data['databaseAdminName'])))
    #     # cur.execute(sql.SQL("GRANT all privileges ON DATABASE {} TO {}").format(sql.Identifier(setup_data['databaseName']), sql.Identifier(setup_data['databaseAdminName'])))
    # except:
    #     print("Error code 2")
    #     cleaner()
    #     time.sleep(3)
    #     cur.close()
    #     conn.close()
    #     return 0
    
    # cur.close()
    # conn.close()
        
def start ():
    return main()

def main ():
    global conn
    
    connection_parameters = {
        "host": '',
        "port": 5432,
        "user": '',
        "password": ''
    }
    
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
            output = createDatabase(connection_parameters)
            if output == 0:
                return 0;
            
        elif (button == 13 or button == 10) and currentPos == len(menuElements) - 1:
            cleaner()
            print("Goodbye")
            time.sleep(1)
            return 0

start()