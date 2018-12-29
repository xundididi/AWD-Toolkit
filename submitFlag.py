import json
import requests

COOKIE_FILE = "cookies.json"
FLAG_FILE = "record.txt"


def loadRecord(startTime):
    f = open("record.txt").read()
    flags = []
    for l in f:
        l = json.loads(l)
    if int(l["ts"]) > int(startTime):
        flags.append(l["data"])


def submit(flags):
    sess = requests.session()
    sess.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
    # sess.headers["X-Requested-With"] = "XMLHttpRequest"
    cookies = open('cookies.json').read()
    cookies = json.loads(cookies)
    for cookie in cookies:
        sess.cookies[cookie["name"]] = cookie["value"]
    
    for f in flags:
        res = sess.post("http://127.0.0.1/", data={"flag": f})
    print(res.text)