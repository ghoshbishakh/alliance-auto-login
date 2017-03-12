import time
import requests


def login():
    print("Attempting to login..")
    payload = {'user': 'ghoshkanika',
               'pass': 'hakunamatata!1',
               'login': 'Login'}
    requests.post("http://10.254.254.102/0/up/", data=payload)


def main():
    try:
        while(1):
            try:
                r = requests.get('http://news.ycombinator.com/', timeout=5)
                if(r.status_code != 200):
                    login()
                else:
                    print("Logged in")
            except:
                login()

            time.sleep(30)
    except KeyboardInterrupt:
        print("Interrupted")
