import httplib2
import webbrowser

from apiclient.discovery import build
from oauth2client import client 

flow = client.flow_from_clientsecrets(
         'client_secret.json',
         scope=['https://www.googleapis.com/auth/drive.file',
                'https://www.googleapis.com/auth/urlshortener'],
         redirect_uri='urn:ietf:wg:oauth:2.0:oob')

webbrowser.open(flow.step1_get_authorize_url())
auth_code = raw_input('Enter the auth code: ')
credentials = flow.step2_exchange(auth_code)
http = credentials.authorize(httplib2.Http())

service = build('drive', 'v2', http)

body = { 
  'mimeType': 'application/vnd.google-apps.document',
  'title': 'hodor' 
}
file = service.files().insert(body=body).execute()

body = {
  'role': 'writer',
  'type': 'anyone',
  'withLink': True
}
service.permissions().insert(fileId=file['id'], body=body).execute()

file = service.files().get(fileId=file['id']).execute()
share = file['alternateLink']

service = build('urlshortener', 'v1', http)

body = { 'longUrl': share }
short = service.url().insert(body=body).execute()
print short['id']
