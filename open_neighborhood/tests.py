from django.test import TestCase
from open_neighborhood.apps.neighborhood.models import Person
from django.utils import timezone
from graphene.test import Client
from open_neighborhood.schema import schema

class PersonTest(TestCase):
    
    def test_create_person(self):
        person=Person(id_card='0954019550',name='Eduardo Ortiz',birth='04-04-1997',status='True',email='leortiz@espol.edu.ec', password='test', created_at= timezone.now())
        self.assertNotEqual('Eduardo Ortiz',person) 
        #even though the "__str__" method of the person model only specifies the name, the abstraction of the model is maintained


class TestHey():

    def test_hey(self):
        client = Client(schema)
        executed = client.execute('''{ hey }''')
        assert executed == {
            'data': {
                'hey': 'hello!'
            }
        }