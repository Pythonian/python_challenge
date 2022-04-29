import subprocess
import logging

from flask import Flask
from flask import jsonify


app = Flask(__name__)

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO)
logging.info('This is an info message to stdout.')

git_hash = subprocess.check_output(
    ["git", "describe", "--always"]).decode().strip()


@app.route('/helloworld')
def hello():
    return 'Hello Stranger'


@app.route('/versionz')
def project():
    return jsonify(
        git_hash=git_hash,
        project_name='Python challenge')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
