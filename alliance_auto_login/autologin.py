import time
import requests
import sys


def login(username, password):
    print("Attempting to login..")
    payload = {'user': 'ghoshkanika',
               'pass': 'hakunamatata!1',
               'login': 'Login'}
    try:
        requests.post("http://10.254.254.102/0/up/", data=payload)
    except:
        print("Could not connect to alliance server")


def main():
    if len(sys.argv) < 3:
        print("Usage: allianceautologin <username> <password>")
        return
    username = sys.argv[1]
    password = sys.argv[2]
    try:
        while(1):
            try:
                r = requests.get('http://news.ycombinator.com/', timeout=5)
                if(r.status_code != 200):
                    login(username, password)
                else:
                    print("Logged in")
            except:
                login(username, password)

            time.sleep(30)
    except KeyboardInterrupt:
        print("Interrupted")
