import pandas as pd
import mariadb
import sys
import configparser
import os

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

    # ONLY FOR LOCAL TESTING #######################################
    os.environ['AZURE_TENANT_ID'] = config["AZURE"]['AZURE_TENANT_ID']
    os.environ['AZURE_CLIENT_ID'] = config["AZURE"]["AZURE_CLIENT_ID"]
    os.environ['AZURE_CLIENT_SECRET'] = config["AZURE"]["AZURE_CLIENT_SECRET"]
    #############################################################

    print("Credentials")

if __name__ == "__main__":
    main()