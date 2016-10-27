import requests
from email.utils import parsedate_to_datetime

URL = "http://training.securitum.com/rozwal/podstawowka/podstawowka_2.php"

from hashlib import md5
def md5_file(filename):
    crc = md5()
    fp = open(filename, 'rb')
    for i in fp:
        crc.update(i)
    fp.close()
    return crc.hexdigest()
params={}
files={}
def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
params = {'ROZWAL':md5_file('ROZWAL.txt')}
files = {'ROZWAL': open('ROZWAL.txt', 'rb')}
r = requests.post(URL, params=params, files=files)
pretty_print_POST(r.request)
print(r.text)