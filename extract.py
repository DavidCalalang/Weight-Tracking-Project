from googleapiclient.discovery import build
from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle

SCOPES = ['https://www.googleapis.com/auth/keep']
CLIENT_SECRET_FILE = 'client_secret.json'
REDIRECT_URI = 'http://localhost:8080/'


def get_credentials():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES, redirect_uri=REDIRECT_URI)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

print("foo1")
creds = get_credentials()
service = build('keep', 'v1', credentials=creds)
print("foo2")
# List notes
results = service.notes().list().execute()
notes = results.get('notes',)

if not notes:
    print('No notes found.')
else:
    print('Notes:')
    for note in notes:
        print(f"- {note['title']}: {note.get('body', {}).get('textContent', '')}")


"""
# Load credentials from the client secrets file
flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRET_FILE, SCOPES, redirect_uri=REDIRECT_URI
)

creds = flow.run_local_server(port=8080)

service = build('keep', 'v1', credentials=creds)

results = service.notes().list().execute()
notes = results.get('items', [])

if not notes:
    print('No notes found.')
else:
    print('Notes:')
    for note in notes:
        print(f"- {note['title']}")
"""