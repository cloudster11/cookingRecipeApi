from os import listdir
import sqlite3
import json


def main():
    connection = sqlite3.connect(":memory:")
    cur = connection.cursor().executescript(open("database_mask.sql").read())
    connection.commit()
    cur.close()

    for fileName in listdir("Files"):
        # Add Name and ID to Recipe Table
        content = json.load(open("Files/" + fileName))
        name = content["Name"]
        sqlQueryRec = f"INSERT INTO Recipies(ID_Rec, Name) VALUES (\"{(fileName[0:5])}\", \"{name}\");"
        connection.cursor().executescript(sqlQueryRec)

        # Get New Tags
        tags = content["Tags"].split(", ")
        cur = connection.cursor().execute("SELECT * FROM TAGS")
        knownTags = []
        for x in cur.fetchall():
            knownTags += x

        # Add new tags to tag table
        newTags = list(set(tags) - set(knownTags))
        sqlQueryInsertNewTags = ""
        for tag in newTags:
            sqlQueryInsertNewTags += f"INSERT INTO TAGS(Name) VALUES (\"{tag}\");"
        connection.cursor().executescript(sqlQueryInsertNewTags)

        # Fill RecHasTag Table
        sqlQueryRecHasTag = ""
        for tag in tags:
            sqlQueryRecHasTag += f"INSERT INTO RecHasTag (ID_Rec, Name) VALUES (\"{fileName[0:5]}\", \"{tag}\");"
        connection.cursor().executescript(sqlQueryRecHasTag)
        # Commit Changes
        connection.commit()

    # GET SQL STATEMENT
    sqlFile = open("database.sql", "w")
    for line in connection.iterdump():
        sqlFile.write(line)

if __name__ == "__main__":
    main()
