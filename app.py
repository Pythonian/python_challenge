import subprocess
import logging

import re
from flask import Flask, request
from flask import jsonify


app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost.localdomain:5000'


logging.basicConfig(
    format='ISO DATE: %(asctime)s MESSAGE: %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO)
logging.info(
    'This is an info message to stdout.'
)

git_hash = subprocess.check_output(
    ["git", "describe", "--always"]).decode().strip()


@app.route('/hello/')
def hello():
    return 'Hello Stranger'


@app.route('/helloworld/')
def helloworld():
    name = request.args.get('name')
    seperated_name = re.sub("([A-Z])", " \\1", name).strip()
    if name:
        return f'Hello {seperated_name}'
    else:
        return 'Hi there'


@app.route('/versionz/')
def versionz():
    return jsonify(
        git_hash=git_hash,
        project_name='Python challenge')


# if __name__ == '__main__':
#     app.run(debug=True, port=8080)
