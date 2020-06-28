import unittest
import json
import mock
from wsgi import create_app
from flask import jsonify


class TestUpdateWebHook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(environment="testing")

    def setUp(self):
        with self.app.app_context():
            self.app.testing = True
            self.app = self.app.test_client()

            self.trigger = {
                "message": "play"
            }
            self.updateData = {
                "message": ""
            }

            self.updateFailData = {
                "message": ""
            }

    def test_successful_update_web_hook(self):
        """ Test that the update web hook returns a successful response """
        response = self.app.post('/update/', data=json.dumps(self.updateData), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_failed_update_web_hook(self):
        """ Test that the update web hook returns a failed response """
        response = self.app.post('/update/', content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # configure chat rooms: Geography, History, Entertainment
    # customer sends 'play'
    # system generates a response: 'welcome to vonage qna ..... '
    # question 1: multiple choice answers, A,B,C,D
    # question 2:
    # question 3:
    # ....
    # question 10:
    # full results: points earned from correct answers

    def test_qna_trigger(self):
        """ Test that the QnA app is triggered by the end user sending play and returns the correct response """
        # update_hook_response = mock.Mock()
        test_text = "Welcome to Vonage QnA"
        response = self.app.post('/update/', data=json.dumps(self.trigger), content_type='application/json')

        self.assertEqual(test_text, response.json)


if __name__ == "__main__":
    unittest.main()
