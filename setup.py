import os
import time
import sys
import gk
import getpass
import json
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
    name = ''
    password = ''
    
    while True:
        print(art)
        name = input("Username: ")
        
        password = passwordHider("Password: ")
        
        print(f"\n{password}")
        
def passwordHider(prompt):
    print(prompt, end="", flush=True)
  
    password = ""
  
    while True:
        ch = gk.getkeyInASCII()
        if ch == 13 or ch == 10:
            break
        elif ch == 8:
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password = str(password) + str(chr(ch))
            print(f"{chr(ch)}", end="", flush=True)
            time.sleep(0.15)
            print("\b \b", end="", flush=True)
            print("*", end="", flush=True)
    return password

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