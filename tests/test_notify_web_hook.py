import unittest
import json
import mock
from wsgi import create_app
from flask import jsonify


class TestNotifyWebHook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(environment="testing")

    def setUp(self):
        with self.app.app_context():
            self.app.testing = True
            self.app = self.app.test_client()

    def test_notify_web_hook(self):
        """ Test that the notify web hook returns a successful response """
        response = self.app.get('/notify/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
