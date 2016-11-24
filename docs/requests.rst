HTTP in Python with :py:mod:`requests`
======================================================

Short intro to HTTP
-----------------------

Each time a browser needs to fetch a file from a server it uses a protocol called HTTP (HyperText Transfer Protocol).
In HTTP the client sends a request for some resource and receives a response from the server with information about the resource and the resoure itself.

What is an HTTP request?
++++++++++++++++++++++++++++

The basic structure of an HTTP request is the following:

    #. A Request-line consisting the request method

    #. Zero or more header lines followed by a CRLF (end of the line characters basically)

    #. An empty line indicating the end of the request's header

    #. Optionally a message-body

Example GET request sent to google.com from Firefox browser:

.. code-block:: none

    GET /v3/links/fetch/en-US/default HTTP/1.1
    Host: tiles.services.mozilla.com
    User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Content-Type: application/json
    Connection: close


The body of the above request is empty.

HTTP request methods
++++++++++++++++++++++++++++

HTTP requests use different methods to indicate the operation to be performed on the requested resource. The most commonly used are:

#. GET

    The GET method is used to retrieve information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data.

#. POST

    A POST request is used to send data to the server, for example, customer information, file upload, etc. using HTML forms.

#. PUT

    Replaces all the current representations of the target resource with the uploaded content.

#. DELETE

    Removes all the current representations of the target resource given by URI.

HTTP Response
++++++++++++++++++++++++++++

HTTP Response has the following structure:

    #. A Status-line

    #. Zero or more header fields followed by CRLF (end of line charachters)

    #. An empty line

    #. Optionally a message-body


In case of HTTP requests sent by a browser, the message body typically contains the HTML code of the requested web page.

Response status codes
++++++++++++++++++++++++++++

Status code of a response is a 3-digit integer, where the first digit indicates the category of the response:

1 	1xx: Informational
    It means the request was received and the process is continuing.

2 	2xx: Success
    It means the action was successfully received, understood, and accepted.

3 	3xx: Redirection
    It means further action must be taken in order to complete the request.

4 	4xx: Client Error
    It means the request contains incorrect syntax or cannot be fulfilled.

5 	5xx: Server Error
    It means the server failed to fulfill an apparently valid request.

Successful requests have typically the status code 200, the status 404 indicates that the requested resource has not been found.


:py:mod:`requests` module
----------------------------------------

To work with HTTP requests we will use the third-party library :py:mod:`requests`.
It's not a part of the standard library, but currently it's the standard way to go about HTTP with Python.

It can be installed with pip by typing:

.. code-block:: none

    python3 -m pip install requests

or

.. code-block:: none

    pip install requests

if pip for the right version of python is available in your PATH

Try to install :py:mod:`requests` within your virtual environment only.


Sending a simple GET request
++++++++++++++++++++++++++++++++++++

.. code-block:: python

    import requests

    response = requests.get('http://www.python.org')
    print(response.status_code)
    print(response.headers['Date'])
    print(response.text)


Authentication
+++++++++++++++++++++++++++++++++++++++

:py:mod:`requests` support a wide variety of authentication methods. For the training we will need only the basic HTTP Authentication

.. code-block:: python

    import requests
    from requests.auth import HTTPBasicAuth

    auth = ('my_username', 'my_password')

    r = requests.get(URL, auth=auth, params=payload)


Go to :ref:`req00`

Request parameters
++++++++++++++++++++++++++++

HTTP requests can have additional parameters, used for example for sending data from user forms.

For example, if a login page has uses the following form:

.. code-block:: html

    <form action="index.php" method="POST">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit" value="Login" />
    </form>

You can generate a corresponding request by using POST method with username and password provided in params dictionary

.. code-block:: python

    import requests

    my_params = {'username':'my_username', 'password':'my_password'}
    r = requests.post(URL, params=my_params)

.. _req00:

Excercise REQ00: Basic HTTP Authentication
--------------------------------------------------

Tasks
++++++++

#. Send a GET request to one of LSYP intranet pages. Use ``HTTPBasicAuth`` object to to provide your credentials.
#. You can store them temporarily in an external module and import to your script as variables or get from the user with :py:func:`input`

:ref:`REQ00_solution`

Excercise REQ01: Exploiting a Blind SQL Injection vulnerability
---------------------------------------------------------------------------

The service http://overthewire.org/wargames/ offers a large set of so called wargames, i.e. challenges that help you to learn and practice various IT-security concepts.

The series "natas" concentrates on web applications. To enter each of the levels you need a password that is obtained by solving the previous puzzle.
Today we will solve the level 16 which deals with the vulnerability called Blind SQL Injection

What is an SQL Injection?
+++++++++++++++++++++++++++++

According to Wikipedia:

.. pull-quote::

    SQL injection is a code injection technique, used to attack data-driven applications,in which nefarious SQL statements are inserted into an entry field for execution.

    It is mostly known as an attack vector for websites but can be used to attack any type of SQL database.

Practically, if a web application contains an entry field, from which the str  ing is directly put into an SQL query,
there is a risk, that the user would escape the query and execute some logic or operations that were not originally intended by the author of the application.


Let's consider the following query:

.. code-block:: python

    statement = "SELECT * FROM users WHERE name = '" + userName + "';"

If the following string is inserted into this query without any validation or character escapes

.. code-block:: none

    ' OR '1'='1


the "WHERE" section of the query will always return True, and thus - the results of the SELECT will be returned no matter what the original condition was (in this case that the username must be known)


Blind SQL Injection
++++++++++++++++++++++++

Not always the result of a SELECT query are printed directly to on the website. Sometimes it's only some other information like whether or not a user with the given username exists.
In such case we can obtain the sensitive information indirectly by exploiting the so called Blind SQL Injection.

The vulnerable webpage from natas15 uses the following PHP code for executing the query:

.. code-block:: php

    <?php
        # (...)
        $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
        if(array_key_exists("debug", $_GET)) {
            echo "Executing query: $query<br>";
        }

        $res = mysql_query($query, $link);
        if($res) {
        if(mysql_num_rows($res) > 0) {
            echo "This user exists.<br>";
        } else {
            echo "This user doesn't exist.<br>";
        }
        } else {
            echo "Error in query.<br>";
        }
        # (...)
    ?>

As we can see, the "username" variable is inserted directly from the POST request and that creates an SQL injection vulnerability.
However the results of the query to the database are not printed anywhere.

Is the information that the given user exists enough to obtain his password?

SQL LIKE operator
____________________________

The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

The following SQL statement selects all customers with a City starting with the letter "s":
Example:

.. code-block:: sql

    SELECT * FROM Customers
    WHERE City LIKE 's%';

SQL BINARY operator
____________________________

In the considered scenario, LIKE will check the pattern case-insensitively (will return true both when the password starts with A or a, regardless the case)
Use LIKE BINARY to get a case-sensitive results.

Malicious query
____________________________

By combining the original query that checks if the user exists with the additional condition on the password, we can create an injection that will result in the text "This user exists"
displayed only if the user exists AND its password starts with the given letter.


Tasks
+++++++++++++

#. Write a Python script that will find the password for the user natas16
#. Assume that the password is 32 characters long and contains numbers and upper and lower case letters.
#. Use Blind SQL injection with LIKE BINARY operator to check if the user's password starts with some letter.
#. After each request check if the response contains the expected text, "This user exists."
#. If a single check is successful, move on trying to guess the next letter.
#. Print the whole password on the screen and try to login to the next level.


Excercise REQ02: Brute force attack on session id
--------------------------------------------------------------

This example is another level from natas wargame.
In this excercise we will hijack a session by executing a brute force attack on the session id.

We assume that on the server there already exists an authenticated admin session and once we send a request with its id, the password to the next level will be revealed.


What is a session ID?
+++++++++++++++++++++++++++

A session ID in network communication is a piece of data used to identify a series of related message exchanges between the client and the server.
A Session ID is used to identify a logged in user and thus, when stolen, can be used to obtain the user's privileges.
In real systems, session ids are long, randomly generated values to prevent session hijacking by guessing or brute force attacks.

However in this excercise we will simulate an attack on a website that grants session ids as random numbers from a very limited pool.

In PHP session id is stored read from a cookie value ``PHPSESSID``.

To send a cookie with :py:mod:`requests`, use cookies parameter:

.. code-block:: python

    import requests

    # (...)

    requests.post(URL, cookies={'cookie_name', 'cookie_value'})

Tasks
++++++++++

level: http://natas18.natas.labs.overthewire.org

``username: natas18``

``password: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP``

#. Open ``natas18`` in the browser, examine the webpage, check the source and see what data is exchanged with the server (by looking at the name of the input field in the page source)
#. Use Python requests to send a request to the website and print the response
#. Brute force the session id by sending requests with different values of the cookie, assume that the ``PHPSESSID`` value is an integer.
#. Look for a response that reveals the password. Assume that you know that the password is a 32 characters long string of numbers and letters
#. Extract the password from the response and print it on the screen (use regular expressions!)

:ref:`REQ02_solution`