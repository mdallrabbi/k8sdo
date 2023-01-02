import os
from flask import Flask
DB_HOST = os.environ.get('APP_DB_HOST')
DB_USER = os.environ.get('APP_DB_USER')
app = Flask(__name__)
@app.route('/')
def print_config():
    output = 'DB_HOST: {} -- DB_USER:{}'.format(DB_HOST, DB_USER)
    return output
