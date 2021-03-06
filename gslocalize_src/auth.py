import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def authorize():
  creds = None

  if os.path.exists('/usr/local/bin/gslocalize_src/authentication.pickle'):
    with open('/usr/local/bin/gslocalize_src/authentication.pickle', 'rb') as token:
      creds = pickle.load(token)

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          '/usr/local/bin/gslocalize_src/credentials.json', SCOPES)
      creds = flow.run_local_server(port=55832)

    with open('/usr/local/bin/gslocalize_src/authentication.pickle', 'wb') as token:
      pickle.dump(creds, token)

  return creds
