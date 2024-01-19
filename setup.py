import json
import psycopg2
from psycopg2 import sql

with open('setup.json', 'r') as setup:
    setup_data = json.load(setup)
    
connection_parameters = {
    "host": setup_data["host"],
    "port": setup_data["port"],
    "user": setup_data["user"],
    "password": setup_data["password"]
}

conn = psycopg2.connect(
    host = connection_parameters["host"],
    port = connection_parameters["port"],
    user = connection_parameters["user"],
    password = connection_parameters["password"],
)

databaseName = "timeMenager"

cur = conn.cursor()
conn.autocommit = True

cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(databaseName)))

conn.autocommit = False

cur.close()
conn.close()