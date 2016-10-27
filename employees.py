import requests
from my_creds import get_creds
from bs4 import BeautifulSoup
import os

from requests.auth import HTTPBasicAuth
user, passw = get_creds("domain")
URL = "https://userdatabase.lsy.pl/employees/report/employee/active"

auth = HTTPBasicAuth(user, passw)

def get_all_employees():
    r = requests.get(URL, auth=auth, verify=False)
    bs = BeautifulSoup(r.text, 'html.parser')
    all = bs.find_all('a', href=True)
    for e in all:
        if len(e.text.split())==2:
            name = e.text
            number = e['href'].split('/')[-1]
            URL_IMG = 'https://userdatabase.lsy.pl/employees/employee/avatar/{}'.format(number)
            r_img = requests.get(URL_IMG, auth=auth, verify=False, stream=True)
            filepath = os.path.join(os.path.dirname(__file__), 'employees', name+'.jpg')
            with open(filepath, 'wb') as img_file:
                for chunk in r_img:
                    img_file.write(chunk)


r = requests.get(URL, auth=auth, verify=False)

print(r.status_code)
print(r.headers)