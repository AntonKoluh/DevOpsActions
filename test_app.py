import unittest
import json
from app import app

class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_route(self):
        response = self.app.post('/api/products',
            data=json.dumps({'name': 'butter', 'price': 20}),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Product added successfully.')

if __name__ == '__main__':
    unittest.main()