from app import app
import unittest


class FlaskTest(unittest.TestCase):
    
    # init logic for the test suites
    # executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        pass

    # clean up logic for the test suites
    # excuted after all tests in one test run
    @classmethod
    def tearDownClass(cls):
        pass

    
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        self.app.testing = True
        pass

    def tearDown(self):
        pass

    def testIndexStatus(self):

        # HTPP GET request to app
        result = self.app.get('/')
        self.assertEqual(result.status_code,200)

    def testGrabDataStatus(self):
        # app = Flask(__name__)
        result = self.app.get('/grab_data')
        self.assertEqual(result.status_code,200)
    
    def test_GrabDataStatus(self):
        with app.test_client as client:
            send = {'token_data': '{\"card_number\":\"tok_sandbox_5J5j2GQrUxkN5ohBCBPgyX\",\"card_cvc\":\"tok_sandbox_b6wh4zNx9ZRaeqGDY6g8Uv\",\"card_expirationDate\":\"tok_sandbox_pyaqsj2bjX9azsX1Yafto1\"}'}
            result = client.post(
                '/reveal_data',
                data = send    
            )
        yield client
        self.assertEqual(result.status_code, 200)
    
    def testGrabDataStatusNoData(self):
        with app.test_client() as client:
            send = {'token_data': None}
            result = client.post(
                '/reveal_data',
                data = send 
            )
        yield client
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
