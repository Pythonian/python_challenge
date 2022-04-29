import subprocess
import logging

import re
from flask import Flask, request
from flask import jsonify


app = Flask(__name__)

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO)
logging.info('This is an info message to stdout.')

git_hash = subprocess.check_output(
    ["git", "describe", "--always"]).decode().strip()


@app.route('/helloworld/')
def hello():
    name = request.args.get('name')
    seperated_name = re.sub("([A-Z])", " \\1", name).strip()
    if name:
        return f'Hello {seperated_name}'
    else:
        return 'Hello Stranger'


@app.route('/versionz')
def project():
    return jsonify(
        git_hash=git_hash,
        project_name='Python challenge')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
