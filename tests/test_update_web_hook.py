import unittest
from wsgi import create_app


class TestUpdateWebHook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(environment="testing")

    def setUp(self):
        with self.app.app_context():
            self.app.testing = True
            self.app = self.app.test_client()

            self.updateData = {
                "message": ""
            }

            self.updateFailData = {
                "message": ""
            }

    def test_successful_update_web_hook(self):
        """ Test that the update web hook returns a successful response """
        response = self.app.post('/update/', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_failed_update_web_hook(self):
        """ Test that the update web hook returns a failed response """
        response = self.app.post('/update/', content_type='application/json')
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
