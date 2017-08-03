import unittest

from shortening.shortening import app

class ShorteningTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to root and assert status is 200
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_home_default_response(self):
        # sends HTTP GET request to root and assert correct default response
        result = self.app.get('/') 

        # assert the data of the response
        self.assertEqual(result.data, 'Welcome to Shortening')

    def test_different_hash_from_same_string(self):
        # requests two hashes with the same input string
        hash_one = self.app.post('/', data={'url': 'a sample string'})
        hash_two = self.app.post('/', data={'url': 'a sample string'})

        # assert the two hashes are different
        self.assertNotEqual(hash_one, hash_two) 