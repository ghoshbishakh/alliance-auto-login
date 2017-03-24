import time
import requests
import sys
import getpass
from bs4 import BeautifulSoup


url = "http://10.254.254.45/0/up/"

def print_usage():
    print("Usage: allianceautologin [\'--login\' or \'-l\'] \n allianceautologin [\'--status\' or \'-s\'] ")


def login(username, password):
    print("Attempting to login..")
    payload = {'user': username,
               'pass': password,
               'login': 'Login'}
    try:
        requests.post(url, data=payload)
    except:
        print("Could not connect to alliance server")


def login_status():
    r = requests.get('https://news.ycombinator.com/', timeout=5)
    if(r.status_code != 200):
        login(username, password)
    else:
        print("Logged in")


def get_service_status():
    r = requests.get(url).text
    soup = BeautifulSoup(r, "lxml")

    soup = soup.find('table', attrs = {'id': 'thesmalltable'})
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


def service_status(username, password):
    """
    Shows status of service
    """

    # log in if not already 
    login_status()
    get_service_status() 


def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    
    if sys.argv[1] != '--login' and sys.argv[1] != '-l' and sys.argv[1] != '--status' and sys.argv[1] != '-s':
        print_usage()
        return

    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    
    try:
        if sys.argv[1] == '--login' or sys.argv[1] == '-l':
            while(1):
                try:
                    login_status()
                except:
                    login(username, password)

                time.sleep(30)
        elif sys.argv[1] == '--status' or sys.argv[1] == '-s':
            service_status(username, password)
    except KeyboardInterrupt:
        print("Interrupted")
