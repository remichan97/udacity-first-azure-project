import os
from sqlalchemy.engine import URL
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

basedir = os.path.abspath(os.path.dirname(__file__))
# Adapted from the 
vaulturl = f'https://article-vaults.vault.azure.net'
credential = DefaultAzureCredential()
secret = SecretClient(vault_url= vaulturl, credential= credential)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or secret.get_secret('blob-account').value
    # BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'f4hu/yM/9+Xff3BJPnTXykP1wMHggwStABMRVT9aLCGpB93p/3OyxqkkrWzgmKRnUzHGdtX1J07M+ASt+fjDUQ=='
    STORAGE_CONNECTION_STRING = secret.get_secret('storage-connection-string').value
    
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or secret.get_secret('blob-container-images').value

    SQL_SERVER = os.environ.get('SQL_SERVER') or secret.get_secret('sql-server-url').value
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or secret.get_secret('sql-server-database').value
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or secret.get_secret('sql-username').value
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or secret.get_secret('sql-password').value
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = URL.create(
        'mssql+pyodbc',
        username=SQL_USER_NAME,
        password=SQL_PASSWORD,
        host=SQL_SERVER,
        port=1433,
        database=SQL_DATABASE,
        query= {
            "driver": "ODBC Driver 17 for SQL Server"
        }
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    ### Info for MS Authentication ###pyodbc
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = secret.get_secret('authen-secret').value
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = secret.get_secret('authen-client-id').value

    REDIRECT_PATH = "/getAuthToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session