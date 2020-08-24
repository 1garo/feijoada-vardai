from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SAMPLE_SPREADSHEET_ID = '1lfAWrUiF28HR8YphHa2aTWqlgYjR7aTBBJh3XbWcozs'
SAMPLE_RANGE_NAME = '!A:Z'


def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        date_res = []
        name_res = []
        ap_res = []
        bloco_res = []
        type_res = []
        end = len(values[1:])-1
        for i in range(len(values[1:])):
            data = values[1:][i]
            date_res.append(data[0])
            name_res.append(data[1])
            ap_res.append(data[2])
            bloco_res.append(data[3])
            type_res.append(data[4])

    print('data: {}'.format(date_res))
    print('tipo: {}'.format(type_res))
    print('name: {}'.format(name_res))
    print('ap: {}'.format(ap_res))
    print('bloco: {}'.format(bloco_res))


if __name__ == '__main__':
    main()
