import mariadb

from dotenv import load_dotenv
from os import getenv

load_dotenv()

connect = mariadb.connect(
    host=getenv("HOST"),
    port=int(getenv("PORT")),
    user=getenv("USER_NAME"),
    password=getenv("PASSWORD"),
    database=getenv("DATABASE"),
)
cursor = connect.cursor()

iso_country = input("Enter country code: ")

cursor.execute("""
    SELECT Type, COUNT(*) AS Count
    FROM airport WHERE Iso_country = ?
    GROUP BY Type
    ORDER BY Count DESC
""", (iso_country,))
res = cursor.fetchall()

print(res)