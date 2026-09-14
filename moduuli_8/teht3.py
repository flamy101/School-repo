from geopy.distance import geodesic
import mariadb

from os import getenv
from dotenv import load_dotenv

load_dotenv()

connect = mariadb.connect(
    host=getenv("HOST"),
    port=int(getenv("PORT")),
    user=getenv("USER_NAME"),
    password=getenv("PASSWORD"),
    database=getenv("DATABASE"),
)

cursor = connect.cursor()

def get_cord(icao):
    cursor.execute("""
    SELECT Latitude_deg, Longitude_deg
    FROM airport WHERE Ident = ?
    """ ,(icao,))
    return cursor.fetchone()

def distanceCalc(d1, d2):
    return geodesic(d1, d2).kilometers

print("Enter ICAO-CODES:")
c1 = input("\nFirst: ").upper()
c2 = input("\nSecond: ").upper()

cord1 = get_cord(c1)
cord2 = get_cord(c2)

distance = distanceCalc(cord1, cord2)


print(f"Distance is: {distance:.2f}")

