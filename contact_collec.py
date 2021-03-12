from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from flask import Flask, render_template

class Contact():
    def __init__(self, name, email):
        self.name = name
        self.email = email

class GoogleContactsSearcher():
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']
    
    def _build_search_service(self):
        """Shows basic usage of the People API.
        Prints the name of the first 10 connections.
        """
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
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return build('people', 'v1', credentials=creds)

    def search(self):
        service = self._build_search_service()
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=1000, #100 contacts default changed
            personFields='names,emailAddresses').execute()
        connections = results.get('connections', [])
        persons = []
        for person in connections:
            names = person.get('names', [])
            emails = person.get('emailAddresses', [])
            name = names[0].get('displayName')
            if emails:
                email = emails[0].get('value')
            else:
                email = 'contact@no_email_found.com.br'
            persons.append(Contact(name,email))
        return persons

    def _fetch_email_address(self, email):
        email = str(email)
        email = email.split('@')
        email = email [1]
        point = email.find('.')
        email = email[0:point]
        return email

    def collect_providers(self, list_of_person_type_objects):
        email_keys = []

        for person in list_of_person_type_objects:
            email = self._fetch_email_address(person.email)
            if email not in email_keys:
                email_keys.append(email)
        return email_keys

#returns list of objects with attribute 'email'
searcher = GoogleContactsSearcher()
list_all_peopple = searcher.search()
list_all_providers = searcher.collect_providers(list_all_peopple)

if __name__ == '__main__':
    searcher._build_search_service()
    searcher.search()
    
#Starting Flask server
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', contacts = list_all_peopple, providers = list_all_providers)

#default port 5000 changed for test
app.run(host='127.0.0.1', port=5006)
