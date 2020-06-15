import unittest
import json
from wsgi import create_app


class TestEventWebHook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(environment="testing")

    def setUp(self):
        with self.app.app_context():
            self.app.testing = True
            self.app = self.app.test_client()

            self.eventData = {
                "provider": ""
            }

            self.eventFailData = {
                "provider": ""
            }

    def test_successful_event_web_hook(self):
        """ test that the event web hook returns a successful response """
        response = self.app.get('/event/', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_failed_event_web_hook(self):
        """ test that the event web hook returns a failed response """
        response = self.app.get('/event/', content_type="application/json")
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
