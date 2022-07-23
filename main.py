import sqlite3
import requests

con = sqlite3.connect('recipes.db')

dbcur = con.cursor()

dbcur.execute("""
INSERT INTO Tags (name) Values ("Japanisch")
""")

con.commit()
con.close()
