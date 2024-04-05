# 🚧WIP🚧

# Description

This app let you create template for database structure and simply use it on multiple database servers to create exactly same databases. 

# Simple project to create database in postgres

1. Run ```pip3 install -r requirements.txt```, this will install library which is used for connecting to database.
2. Adjust ```setup.json``` in the way you want your database to look (see format below)
3. Run ```setup.py``` and follow the instructions

# Json format
```
{
    "databaseName": "test",
    "databaseAdminName": "testAdmin",

    "groups":
    {
        "group1_name":
        {
            "select": "False",
            "insert": "False",
            "update": "False",
            "delete": "False",
            "truncate": "False",
            "references": "False",
            "trigger": "False",
            "create": "False",
            "connect": "False",
            "temporary": "False",
            "execute": "False",
            "usage": "False",
            "set": "False",
            "alter system": "False"
        }
    },

    "tabs":
    {
        "tab1_name": 
        {
            "column1_name":
            {
                "datatype": "",
                "length": 0,
                "notNull": "False",
                "unique": "False",
                "primaryKey": "False",
                "check": "False",
                "ckeckKeyCondition": "",
                "ifForeignKey": "False",
                "foreignKey": "",
                "referencesTable": "",
                "referencesKey": "",
                "onDeleteSetNull": "False",
                "onDeleteCascade": "False"
            }
        }
    }
}
```

### Optional variables

Delete those optional lines if you don't want to use them

- databaseAdminName - it's creating an admin user which will automatically have all privleges on that database

# Error codes

1. Database not created