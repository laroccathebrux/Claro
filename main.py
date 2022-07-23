import pandas as pd
import mariadb
import sys
import configparser

def main():
    """
    Load config file with database credentials,
    Connects to the database and processes data
    Define credentials to Azure
    :rtype: object
    """
    config = configparser.ConfigParser()
    config.read('Credentials.ini')

    USER = config["MARIADB"]['USER'] 
    PASS = config["MARIADB"]['PASS']
    HOST = config["MARIADB"]['HOST']
    PORT = config["MARIADB"]['PORT']
    DB   = config["MARIADB"]['DB']

    print("Credentials")

if __name__ == "__main__":
    main()