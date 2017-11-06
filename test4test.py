import requests
import json
from datetime import datetime

def getReq():
    rsp = requests.get('http://127.0.0.1:9090/test_upload.php?ver=1&sn=123')
    print(rsp.text)

def postReq():
    sn = 123
    body = """{{
"sn":"{sn}",
"ctr":"1",
"batt":"87",
"date":"{date}",
"time":"{time}",
"lat":"+55.792924",
"lon":"+37.789442",
"gpsvis":"10",
"gnsvis":"11",
"satused":"6",
"gsmlc":"{gsmlocation}",
"gsmlat":"{gsmlat}",
"gsmlon":"{gsmlon}",
"gsmdate":"{gsmdate}",
"gsmtime":"{gsmtime}"
}}
    """.format(**{
        "sn":sn,
        "gsmlocation":0,
        "date": datetime.now().strftime("%y%m%d"),
        "time": datetime.now().strftime("%H%M%S"),
        "gsmdate": datetime.now().strftime("%y%m%d"),
        "gsmtime": datetime.now().strftime("%H%M%S"),
        "gsmlat": "+55.792923",
        "gsmlon": "+37.789441",
    })
    print(body)
    rsp = requests.post('http://127.0.0.1:9090/test_upload.php?ver=1&sn=123', body)
    print(rsp)

def main():
    getReq()
    postReq()

if __name__ == '__main__':
    main()