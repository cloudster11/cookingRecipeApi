#import requests
#import sqlite3
#import os
#
#databaseName = "database.sql"
#
#
#def getCurrentDatabase():
#    file = requests.get("https://raw.github.com/cloudster11/cookingRecipeApi/master/database.sql")
#    f = open(databaseName, "w")
#    f.write(file.text)
#    f.close()
#    return
#
#
#def sqlQuery(query):
