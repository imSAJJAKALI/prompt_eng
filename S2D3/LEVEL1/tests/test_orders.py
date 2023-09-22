
# tests/test_orders.py

import unittest
from app import app, create_order, update_order_status

class TestOrderManagement(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def test_create_order(self):
        response = create_order("John", ["1", "2"])
        self.assertEqual(response.status_code, 200)

    def test_update_order_status(self):
        create_order("Alice", ["1"])
        response = update_order_status(1, "preparing")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
