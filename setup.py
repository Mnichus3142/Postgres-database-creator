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
        
def start ():
    main()

def main ():
    connection_parameters = {
        "host": '',
        "port": 5432,
        "user": '',
        "password": ''
    }
    
    while True:
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
            
        except:
            print("\n\nWrong creditials")
        

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