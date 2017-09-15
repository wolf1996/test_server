from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from flask import render_template
from datetime import datetime

app = Flask(__name__)
mongo = PyMongo(app)

def hello_world_get():
    sn = request.args.get('sn')
    ver = request.args.get('ver')
    print("sn {} ver {}".format(sn, ver))
    res = """{
    "ctr":"1",
    "cfgLock":"1", "updateTimeMin":"240", "smsEnable":"1",
    "phoneNumber":"+7XXXXXXXXXX", 
    }
    """
    print("done")
    global mongo
    mongo.db.queries.insert({'timestamp': datetime.now(), 'method':'GET', 'sn': str(sn), 'ver': str(ver)})
    return res


def hello_world_post():
    print("POST METHOD START")
    body = request.data
    mongo.db.queries.insert({'timestamp': datetime.now(), 'method':'POST', 'body': str(body)})
    return ""


@app.route('/test_upload.php', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return hello_world_post()
    else:
        return hello_world_get()
    return "Smthng strange", 500


@app.route('/get_logs', methods=['GET'])
def get_logs():
    logs = mongo.db.queries.find().sort("timestamp")
    return render_template('logs.html', logs=logs)

