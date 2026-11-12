from flask import Flask
import mariadb

from os import getenv
from dotenv import load_dotenv

load_dotenv()

connect = mariadb.connect(
    host=getenv("HOST"),
    port=int(getenv("PORT")),
    user=getenv("USER"),
    password=getenv("PASSWORD"),
    database=getenv("DATABASE"),
)

cursor = connect.cursor()
app = Flask(__name__)

@app.route("/airports/<string:icao>", methods=["GET"])
def some(icao):
    cursor.execute("""
    SELECT name, municipality FROM airports
    WHERE ident = ?;
    """, (icao,))
    fetched_data = cursor.fetchone()

    name, municipality = fetched_data

    res = {
        "ICAO": icao,
        "Name": name,
        "Location": municipality,
    }
    return res

if __name__ == "__main__":
    app.run(port=3000, debug=True)