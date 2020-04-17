from app import app
import unittest

class FlaskVGSTest(unittest.TestCase):

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
        result = self.app.get('/')

        self.assertEqual(result.status_code, 200)
    def test_index_status_code(self):
        result = self.app.get('/index')

        self.assertEqual(result.status_code, 200)
    def test_message_status_code(self):
        with app.test_client() as client:
            sent = {'ccn': '1111111111111111', 'cvv': '123', 'exp': '07/24'}
            result = client.post(
                '/add_message',
                data=sent
            )
        yield client
        self.assertEqual(result.status_code, 200)

    def test_forward_status_code(self):
        with app.test_client() as client:
            sent = {'ccn': 'token_aIAdkadfID', 'cvv': 'token_ADkkdaldmnveu', 'exp': 'token_urosOSUDmDLiJyJY'}
            result = client.post(
                '/forward',
                data=sent
            )
        yield client
        self.assertEqual(result.status_code, 200)

    def test_message_status_code_no_input(self):
        with app.test_client() as client:
            sent = {'ccn': None, 'cvv': None, 'exp': None}
            result = client.post(
                '/add_message',
                data=sent
            )
        yield client
        self.assertEqual(result.status_code, 200)

    def test_forward_status_code_no_inpute(self):
        with app.test_client() as client:
            sent = {'ccn': None, 'cvv': None, 'exp': None}
            result = client.post(
                '/forward',
                data=sent
            )
        yield client
        self.assertEqual(result.status_code, 200)