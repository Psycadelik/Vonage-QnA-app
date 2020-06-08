import unittest
import json
from run import app


class TestAnswerWebHook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app

    def setUp(self):
        with self.app.app_context():
            self.app.testing = True
            self.app = self.app.test_client()

            self.answerData = {
                "provider": ""
            }

            self.failAnswerData = {
                "provider": ""
            }

            self.eventData = {
                "provider": ""
            }

            self.eventFailData = {
                "provider": ""
            }

    def test_successful_answer_web_hook(self):
        """ test that the answer hook returns a successful response """
        response = self.app.post('/', data=json.dumps(self.answerData), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_failed_answer_web_hook(self):
        """ test that the answer web hook returns a failed response """
        response = self.app.post('/', data=json.dumps(self.failAnswerData), content_type="application/json")
        self.assertEqual(response.status_code, 400)
