import requests
from email.utils import parsedate_to_datetime

URL = "http://training.securitum.com/rozwal/podstawowka/podstawowka_2.php"

params = {'a':'test'}
files = {'ROZWAL.txt.tmp_name': open('ROZWAL.txt.tmp_name', 'rb')}
r = requests.post(URL, params=params, files=files)
print(r.text)