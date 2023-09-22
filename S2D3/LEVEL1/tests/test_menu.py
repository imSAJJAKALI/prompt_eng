import unittest
import json
from app import app, menu

class TestMenuManagement(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def test_add_dish(self):
        response = self.app.post('/add_dish', data=json.dumps({'dish_id': '1', 'name': 'Burger', 'price': 10, 'available': True}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_dish(self):
        response = self.app.post('/add_dish', data=json.dumps({'dish_id': '2', 'name': 'Pizza', 'price': 12, 'available': True}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/get_dish/2')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['name'], 'Pizza')

if __name__ == '__main__':
    unittest.main()
