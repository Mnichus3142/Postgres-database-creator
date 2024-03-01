import os
import time
import components.gk as gk
import json
import components.passwordHider as passwordHider
import psycopg2
from psycopg2 import sql

art = """
  ____  ____   ___  _       ____  ____     ____                _             
 |  _ \/ ___| / _ \| |     |  _ \| __ )   / ___|_ __ ___  __ _| |_ ___  _ __ 
 | |_) \___ \| | | | |     | | | |  _ \  | |   | '__/ _ \/ _` | __/ _ \| '__|
 |  __/ ___) | |_| | |___  | |_| | |_) | | |___| | |  __/ (_| | || (_) | |   
 |_|   |____/ \__\_\_____| |____/|____/   \____|_|  \___|\__,_|\__\___/|_|   
                                                                             
"""

def cleaner ():
    try:
        os.system('cls')
    except:
        os.system('clear')
        
def createDatabase (connection_parameters):  
    conn = psycopg2.connect(
        host = connection_parameters["host"],
        port = connection_parameters["port"],
        user = connection_parameters["user"],
        password = connection_parameters["password"],
    )
    
    passwordDoNotMatch = True
    password = ""
    
    while passwordDoNotMatch:
        cleaner()
        pass1 = passwordHider.passwordHider("Enter new admin password: ")
        pass2 = passwordHider.passwordHider("Confirm new admin password: ")
        
        if pass1 == pass2:
            passwordDoNotMatch = False
            password = pass1
    
    cleaner()
    print("Creating database from file...")
    
    
    
    # cur = conn.cursor()
    # conn.autocommit = True
    
    # try:
    #     cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name)))
    # except:
    #     print("Not working as expected")
    
    # conn.autocommit = False
    # cur.close()
    # conn.close()

    # time.sleep(5)
        
def start ():
    return main()

def main ():
    connection_parameters = {
        "host": '',
        "port": 5432,
        "user": '',
        "password": ''
    }
    
    conn = 0
    
    ifEstablished = 0
    
    while ifEstablished == 0:
        cleaner()
        print(art)
        
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
            
            conn.close()
            
            ifEstablished = 1
            
        except:
            print("\n\nWrong creditials")
            time.sleep(0.5)
            
    menuElements = ["Create database from json file", "Exit"]
    currentPos = 0        
    
    while True:
        cleaner()
        print(art)    
        
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
            createDatabase(connection_parameters)
            
        elif (button == 13 or button == 10) and currentPos == len(menuElements) - 1:
            cleaner()
            print("Goodbye")
            time.sleep(1)
            return 0
        

# with open('setup.json', 'r') as setup:
#     setup_data = json.load(setup)
    
# connection_parameters = {
#     "host": setup_data["host"],
#     "port": setup_data["port"],
#     "user": setup_data["user"],
#     "password": setup_data["password"]
# }

# conn = psycopg2.connect(
#     host = connection_parameters["host"],
#     port = connection_parameters["port"],
#     user = connection_parameters["user"],
#     password = connection_parameters["password"],
# )

# databaseName = "timeMenager"

# cur = conn.cursor()
# conn.autocommit = True

# cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(databaseName)))

# conn.autocommit = False

# cur.close()
# conn.close()

start()