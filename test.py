from app import app
import unittest

class VGS_App_Testing(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        pass

    
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

    def test_Home_Page_status_code(self):

        #Testing the status code of the home page 

        result = self.app.get('/')
        self.assertEqual(result.status_code,200)
        
    def test_add_message_status(self):

        #Testing the status code of the message.html page

        result = self.app.get('/add_message')
        self.assertEqual(result.status_code,200)
    
    def test_GrabDataStatus(self):

        #Testing the revealing of data
        
        with app.test_client as client:
            send = {'json_data': '{\"card_number\":\"tok_sandbox_qqUPZzi7gegTkZSWB4j7pb\",\"card_cvc\":\"tok_sandbox_ejRcz8V1YioqEZWDpwSYvj\",\"card_expirationDate\":\"tok_sandbox_h8qoTeAPx7h6bdUJR36ujL\"}'}
            result = client.post(
                '/forward',
                data = send    
            )
        yield client
        self.assertEqual(result.status_code, 200)
    
    def testGrabDataStatusNoData(self):

        #Testing the revealing of "no" data

        with app.test_client() as client:
            send = {'json_data': None}
            result = client.post(
                '/forward',
                data = send 
            )
        yield client
        self.assertEqual(result.status_code, 200)



if __name__ == '__main__':
    unittest.main()

