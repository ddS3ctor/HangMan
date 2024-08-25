import json
import unittest
from app import app

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_get_words(self):
        response = self.client.get('/words')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertTrue(all(isinstance(word, str) for word in data))
        self.assertGreater(len(data), 0)
        self.assertIn('python', data)
        self.assertIn('hangman', data)
        self.assertIn('challenge', data)
        self.assertIn('programming', data)
        self.assertIn('developer', data)


if __name__ == '__main__':
    unittest.main()