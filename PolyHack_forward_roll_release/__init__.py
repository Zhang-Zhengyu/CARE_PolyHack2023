import os
from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = os.urandom(16)

@app.after_request
def set_response_encoding(response):
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response