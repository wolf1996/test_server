from flask import Flask
from flask import request
from flask import jsonify
from flask import json

app = Flask(__name__)


def hello_world_get():
    print("GET METHOD START")
    sn = request.args.get('sn')
    ver = request.args.get('ver')
    print("sn {} ver {}".format(sn, ver))
    res ="""
    {
    "ctr":"1",
    "cfgLock":"1", "updateTimeMin":"240", "smsEnable":"1",
    "phoneNumber":"+7XXXXXXXXXX", }
    """
    return res


def hello_world_post():
    print("POST METHOD START")
    body = request.data
    print(body)
    return ""


@app.route('/test_upload.php', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return hello_world_post()
    else:
        return hello_world_get()
    return "1"
