import re
import socket
import logging
import subprocess

from flask import Flask, request, jsonify

logging.basicConfig(
    format='ISO DATE: %(asctime)s MESSAGE: %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO)
logging.info(
    'This is an info message to stdout.'
)

git_hash = subprocess.check_output(
    ["git", "describe", "--always"]).decode().strip()


def create_app():
    """
    Creates a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__)

    @app.route('/hello/')
    def hello():
        """
        Render a Hello Stranger response.

        :return: Flask response
        """
        return 'Hello Stranger'

    @app.route('/helloworld/')
    def helloworld():
        name = request.args.get('name')
        if name:
            seperated_name = re.sub("([A-Z])", " \\1", name).strip()
            return f'Hello {seperated_name}'
        return 'Hi there'

    @app.route('/health/')
    def health():
        return jsonify(
            status="UP")

    @app.route('/versionz/')
    def versionz():
        """ Render a JSON response. """
        hostname = socket.gethostname()
        return jsonify(
            hostname=hostname,
            host_ip=socket.gethostbyname(hostname),
            ip=request.remote_addr,
            git_hash=git_hash,
            project_name='Python challenge')

    return app
