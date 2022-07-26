import pandas as pd
import mariadb
import sys
import configparser
from azure.storage.blob import BlobServiceClient

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

    ACCKEY  = config["AZURE"]["ACCKEY"]
    CONTAINER = config["AZURE"]["CONTAINER"]

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

    df_rel_ate_resumolocal     = pd.read_sql("select * from rel_ate_resumolocal", conn)
    df_rel_pro_estoquefisico   = pd.read_sql("select * from rel_pro_estoquefisico", conn)
    df_uti_controleresidencial = pd.read_sql("select * from uti_controleresidencial", conn)
    df_uti_met_local           = pd.read_sql("select * from uti_met_local", conn)
    df_uti_met_vendedor        = pd.read_sql("select * from uti_met_vendedor", conn)
    df_uti_statusged           = pd.read_sql("select * from uti_statusged", conn)

    blob_service_client = BlobServiceClient.from_connection_string(ACCKEY)
    container_client = blob_service_client.get_container_client(CONTAINER)

    print("Saving CSV files...")

    output = df_rel_ate_resumolocal.to_csv(index=False, encoding="utf-8")
    blob_client = container_client.get_blob_client("rel_ate_resumolocal.csv")
    blob_client.upload_blob(output, blob_type="BlockBlob", overwrite=True)

    output = df_rel_pro_estoquefisico.to_csv(index=False, encoding="utf-8")
    blob_client = container_client.get_blob_client("rel_pro_estoquefisico.csv")
    blob_client.upload_blob(output, blob_type="BlockBlob", overwrite=True)

    output = df_uti_controleresidencial.to_csv(index=False, encoding="utf-8")
    blob_client = container_client.get_blob_client("uti_controleresidencial.csv")
    blob_client.upload_blob(output, blob_type="BlockBlob", overwrite=True)

    output = df_uti_met_local.to_csv(index=False, encoding="utf-8")
    blob_client = container_client.get_blob_client("uti_met_local.csv")
    blob_client.upload_blob(output, blob_type="BlockBlob", overwrite=True)

    output = df_uti_met_vendedor.to_csv(index=False, encoding="utf-8")
    blob_client = container_client.get_blob_client("uti_met_vendedor.csv")
    blob_client.upload_blob(output, blob_type="BlockBlob", overwrite=True)

    output = df_uti_statusged.to_csv(index=False, encoding="utf-8")
    blob_client = container_client.get_blob_client("uti_statusged.csv")
    blob_client.upload_blob(output, blob_type="BlockBlob", overwrite=True)
    
    
    print("CSV files saved")

if __name__ == "__main__":
    main()