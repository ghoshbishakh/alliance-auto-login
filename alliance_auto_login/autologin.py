import time
import requests
import sys
import getpass
from bs4 import BeautifulSoup



def print_usage():
    print("Usage: allianceautologin [\'--login\' or \'-l\'] \n \
           allianceautologin [\'--status\' or \'-s\'] ")


def login(url, username, password):
    print("Attempting to login..")
    payload = {'user': username,
               'pass': password,
               'login': 'Login'}
    try:
        requests.post(url, data=payload)
        print("Logged In")
    except:
        print("Could not connect to alliance server")


def login_status():
    try:
        r = requests.get('https://news.ycombinator.com/', timeout=5)
        if(r.status_code != 200):
            print("Not Logged In")
            return False
        else:
            print("Logged In")
            return True
    except:
        print("Not Logged In")
        return False


def get_service_status(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, "lxml")

    soup = soup.find('table', attrs={'id': 'thesmalltable'})
    rows = soup.find_all('tr')

    # show only name, client id, package and expiry date
    name = rows[0].find_all('td')[1].text
    print("NAME: ", name)
    client_id = rows[2].find_all('td')[1].text
    print("CLIENT ID: ", client_id)
    package = rows[3].find_all('td')[1].text
    print("PACKAGE: ", package)
    expiry = rows[4].find_all('td')[1].text
    print("EXPIRY: ", expiry)


def service_status(url, username, password):
    """
    Shows status of service
    """
    # log in if not already
    login(url, username, password)
    get_service_status(url)


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    try:
        if (len(sys.argv) == 5 and
                (sys.argv[1] == '--login' or sys.argv[1] == '-l')):
            url = sys.argv[2]
            username = sys.argv[3]
            password = sys.argv[4]

            while(1):
                print("Running cycle ..")
                print("Checking if logged in ..")
                if not login_status():
                    print("Trying to log in ..")
                    login(url, username, password)

                time.sleep(30)

        elif sys.argv[1] == '--login' or sys.argv[1] == '-l':
            url = input('Enter login url (eg: http://10.254.254.45/0/up/): ')
            username = input('Enter username: ')
            password = getpass.getpass('Enter password: ')

            while(1):
                print("Running cycle ..")
                print("Checking if logged in ..")
                if not login_status():
                    print("Trying to log in ..")
                    login(url, username, password)

                time.sleep(30)
        elif sys.argv[1] == '--status' or sys.argv[1] == '-s':
            url = input('Enter login url (eg: http://10.254.254.45/0/up/): ')
            username = input('Enter username: ')
            password = getpass.getpass('Enter password: ')
            service_status(url, username, password)

    except KeyboardInterrupt:
        print("Interrupted")


if __name__ == '__main__':
    main()
