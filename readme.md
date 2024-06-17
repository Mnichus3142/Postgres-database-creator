# Version 1.0

# Description

This app let you create template for database structure and simply use it on multiple database servers to create exactly same, simple databases. 

# Simple project to create database in postgres

1. Run ```pip3 install -r requirements.txt```, this will install library which is used for connecting to database.
2. Adjust ```setup.json``` in the way you want your database to look (see format below)
3. Run ```main.py``` and follow the instructions

# Json format
```
{
    "databaseName": "(put it here)",
    "databaseAdminName": "(put it here)",

    "tabs":
    {
        "tab1_name(put it here)": 
        {
            "column1_name(put it here)":
            {
                "datatype": "(put it here)",
                "length": (put int here),
                "notNull": "(put True/False here)",
                "unique": "(put True/False here)",
                "primaryKey": "(put True/False here)"
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
2. User already exist and couldn't be dropped
3. User not created
4. Unable to create table(s)