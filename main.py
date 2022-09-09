import sqlite3
import requests
from tkinter import *
from tkinter import ttk
from github import Github


# Get Current Version of Database
databaseName = "database.sql"
file = requests.get("https://raw.github.com/cloudster11/cookingRecipeApi/master/database.sql")
f = open(databaseName, "w")
f.write(file.text)
f.close()


# TODO: Check for database version and just update to newer version to safe traffic
#g = Github("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")
#repo = g.get_user().get_repo("cookingRecipeApi")
#print(repo.get_contents(""))



connection = sqlite3.connect(":memory:")
cur = connection.cursor().executescript(open("database.sql").read())
connection.commit()
cur.close()

def getTags():
    cur = connection.cursor()
    cur.execute("SELECT Name FROM Tags")
    connection.commit()
    tagList = cur.fetchall()
    cur.close()
    return tagList



def getRecipe(id):
    recipeFile = requests.get(f"https://raw.github.com/cloudster11/cookingRecipeApi/master/files/{id}.json")
    print(recipeFile)



















#functions.getCurrentDatabase()
#
#connection = sqlite3.connect(":memory:")
#cur = connection.cursor().executescript(open("database.sql").read())
#print(cur.fetchall())
#connection.commit()
#cur.close()
#
#
##cur = connection.cursor()
##cur.executescript("INSERT INTO Tags (Name) VALUES ('TEST')")
##print(cur.fetchall())
##connection.commit()
##cur.close()
#
#cur = connection.cursor()
#cur.execute("SELECT Name FROM Tags")
#connection.commit()
#print(cur.fetchall())
#cur.close()
#
#connection.close()
