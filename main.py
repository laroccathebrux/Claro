import pandas as pd
import mariadb
import sys
import configparser

config = configparser.ConfigParser()
config.read("credentials.ini")

HOST = config["MARIADB"]["HOST"]
PORT = config["MARIADB"]["PORT"]
USER = config["MARIADB"]["USER"]
PASS = config["MARIADB"]["PASS"]
DBSE = config["MARIADB"]["DBSE"]

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=USER,
        password=PASS,
        host=HOST,
        port=PORT,
        database=DBSE

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()