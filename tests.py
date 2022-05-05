import unittest
import subprocess
from app import create_app
from flask import url_for

git_hash = subprocess.check_output(
    ["git", "describe", "--always"]).decode().strip()


class TestPage(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    def test_hello_page(self):
        with self.app.app_context(), self.app.test_request_context():
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
        with self.app.app_context(), self.app.test_request_context():
            response = self.client.get(url_for('versionz'))
            self.assertEqual(
                response.json,
                {'git_hash': git_hash,
                 'project_name': 'Python challenge'})


if __name__ == '__main__':
    unittest.main()
