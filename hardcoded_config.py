from flask import Flask
DB_HOST = 'mydb.mycloud.com'
DB_USER = 'rabbi'
app = Flask(__name__)
@app.route('/')
def print_config():
    output = 'DB_HOST: {} -- DB_USER: {}'.format(DB_HOST, DB_USER)
    return output
