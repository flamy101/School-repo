import mariadb

from dotenv import load_dotenv
from os import getenv

load_dotenv()

connection = mariadb.connect(
    host=getenv("HOST"),
    port=int(getenv("PORT")),
    user=getenv("USER_NAME"),
    password=getenv("PASSWORD"),
    database=getenv("DATABASE"),
)

cursor = connection.cursor()

icao_input = input("Enter ICAO-code: ")

cursor.execute("SELECT Name FROM airport WHERE Ident = ?", (icao_input,))
res = cursor.fetchall()

print(res)


