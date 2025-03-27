from dotenv import load_dotenv
import os
import import_spreadsheet
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def configure():
    load_dotenv()

def main():
    configure()

    # Skipping gkeep for now, pain
    #master_token = os.getenv('master_token')

    spreadsheet_data = import_spreadsheet.import_data()

    print(spreadsheet_data)


if __name__ == "__main__":
    main()