# 🚧WIP🚧

# Simple project to create database in postgres

1. Run ```pip3 install -r requirements.txt```, this will install library which is used for connecting to database.

# Json format
```
{
    "databaseName": "",
    "databaseAdminName": "",
    "databaseUsersGroup": "True",
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
    "tab2_name": 
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
```

### Optional variables

- databaseAdminName - it's creating an admin user which will automatically have all privleges on that database

# Error codes

1. Database not created