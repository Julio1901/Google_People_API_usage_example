from unittest import TestCase
import unittest
from conectaNuvem import GoogleContactsSearcher, Contact

class TestGoogleContactsSearcher(TestCase, GoogleContactsSearcher):

    def test_search(self):
        service = self._build_search_service()
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=1000,
            personFields='names,emailAddresses').execute()
        
        connections = results.get('connections', [])
        
        persons = []

        for person in connections:
            names = person.get('names', [])
            emails = person.get('emailAddresses', [])
            if names:
                name = names[0].get('displayName')
            if emails:
                email = emails[0].get('value')
            else:
                email = 'email@contato_sem_email.com.br'
            persons.append(Contact(name,email))
        
            expeted_type = "<class 'list'>"
            returned_object = type(persons)
            returned_object = str(returned_object)
            checking_types_of_objects_in_the_people_list= all(isinstance(x, Contact) for x in persons)
            self.assertEqual(expeted_type, returned_object)
            self.assertEqual(checking_types_of_objects_in_the_people_list, True)

    def test_fetch_email_address(self):
        email = 'test.exemple@gmail.com'
        email = email.split('@')
        email = email [1] 
        point = email.find('.')
        email = email[0:point]
        expected_return = 'gmail'
        self.assertEqual(expected_return, email)

    def test_collect_providers(self):
        peoples_email_list = ['julio@gmail.com', 'ezechias@casasaopedro.com']

        email_keys = []

        for people_email in peoples_email_list:
            email = str(people_email)
            email = email.split('@')
            email = email [1]
            point = email.find('.')
            email = email[0:point]
            if not email in email_keys:
                email_keys.append(email)
       
            expeted_email_type = all(isinstance(i, str) for i in email_keys )
            self.assertEqual(expeted_email_type, True)

if __name__ == '__main__':
    unittest.main()

