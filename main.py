import pandas as pd
import mariadb
import sys
import configparser

def getData(cur):
    """
    cur.execute(
    "SELECT first_name,last_name FROM employees WHERE first_name=?", 
    (some_name,))

    for (first_name, last_name) in cur:
        print(f"First Name: {first_name}, Last Name: {last_name}")
    """
    return True

def main():
    """
    Load config file with database credentials,
    Connects to the database and processes data
    :rtype: object
    """

    config = configparser.ConfigParser()
    config.read("credentials.ini")

    HOST = config["MARIADB"]["HOST"]
    PORT = int(config["MARIADB"]["PORT"])
    USER = config["MARIADB"]["USER"]
    PASS = config["MARIADB"]["PASS"]
    DBSE = config["MARIADB"]["DBSE"]

    print(USER)

    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user     = USER,
            password = PASS,
            host     = HOST,
            port     = PORT,
            database = DBSE

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    df_rel_ate_resumolocal = pd.read_sql("select * from rel_ate_resumolocal", cur);

    print(df_rel_ate_resumolocal.head(5))

if __name__ == "__main__":
    main()