import unittest
from app import app
from flask import url_for


class TestPage(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    def test_hello_page(self):
        response = self.client.get(url_for('hello'))
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert 'Hello Stranger' in html

    def test_invalid_page(self):
        response = self.client.get('/invalid/')
        assert response.status_code == 404

    # def test_helloworld_page(self):
    #     response = self.client.get(url_for('helloworld'))
    #     assert response.status_code == 200
    #     html = response.get_data(as_text=True)
    #     assert 'Hello Stranger' in html

    def test_versionz(self):
        response = self.client.get(url_for('versionz'))
        self.assertEqual(
            response.json,
            {'git_hash': '4211457',
             'project_name': 'Python challenge'})


if __name__ == '__main__':
    unittest.main()
