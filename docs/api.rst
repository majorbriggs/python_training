Working with APIs
==========================

A web API is a set of  programming instructions and standards for accessing web
based software applications. APIs base on exchange of HTTP requests, where both the request and the response contain a standardized set of fields.

Many APIs have language specific wrappers that simplify their usage, by replacing the exchange of raw HTTP requests with calling methods on API objects in the respective language.

JIRA API
-------------------------

From `JIRA API documentation <https://developer.atlassian.com/jiradev/jira-apis/jira-rest-apis?_ga=1.100540766.1506016697.1468406647>`_:

.. pull-quote::

    The Atlassian REST APIs provide a standard interface for interacting with JIRA and our other applications.

    REST APIs provide access to resources (data entities) via URI paths.
    To use a REST API, your application will make an HTTP request and parse the response.
    Your methods will be the standard HTTP methods like GET, PUT, POST and DELETE.
    REST APIs operate over HTTP(s) making it easy to use with any programming language or framework.
    The input and output format for the JIRA REST APIs is JSON.


Access JIRA API with :py:mod:`requests`
---------------------------------------------------

JIRA API can be used by making HTTP requests and extracting the information from the JSON response.
We'll start with an example of such approach implemented with :py:mod:`requests`. We use a publicly accessible JIRA instance of Apache project.

.. code-block:: python

    import requests
    import json
    URL = "https://issues.apache.org/jira/rest/api/2/issue/ZOOKEEPER-2613"

    r = requests.get(URL)

    json_dict = r.json() # a standard python dictionary
    print(json.dumps(json_dict, indent=3)) # to pretty-print with 3 spaces of indentation


.. hint::

    If the JIRA instance required a login to browse the issue, we would provide the credentials using ``HTTPBasicAuth``


The response from of the above request is a a JSON formatted representation of the JIRA ticket: (excerpt below)

.. code-block:: json

    {
       "key": "ZOOKEEPER-2613",
       "expand": "renderedFields,names,schema,transitions,operations,editmeta,changelog",
       "id": "13011427",
       "fields": {
          "status": {
             "iconUrl": "https://issues.apache.org/jira/images/icons/statuses/open.png",
             "id": "1",
             "description": "The issue is open and ready for the assignee to start work on it.",
             "name": "Open",
             "self": "https://issues.apache.org/jira/rest/api/2/status/1",
             "statusCategory": {
                "key": "new",
                "id": 2,
                "name": "New",
                "self": "https://issues.apache.org/jira/rest/api/2/statuscategory/2",
                "colorName": "blue-gray"
             }
          },
          "issuetype": {
             "iconUrl": "https://issues.apache.org/jira/images/icons/issuetypes/bug.png",
             "id": "1",
             "description": "A problem which impairs or prevents the functions of the product.",
             "name": "Bug",
             "self": "https://issues.apache.org/jira/rest/api/2/issuetype/1",
             "subtask": false
          },
       },
       "self": "https://issues.apache.org/jira/rest/api/2/issue/13011427"
    }

.. hint::

    From wikipedia:

    JSON (canonically pronounced /ˈdʒeɪsən/) is an open-standard format that uses human-readable text to transmit data objects consisting of attribute–value pairs.
    It is the most common data format used for asynchronous browser/server communication, largely replacing XML which is used by AJAX.
    JSON is a language-independent data format. It derives from JavaScript, but as of 2016 many programming languages include code to generate and parse JSON-format data.
    The official Internet media type for JSON is application/json. JSON filenames use the extension .json.

    In Python, json format can be conveniently processed with :py:mod:`json` package from the standard library


Data from a JSON response may be loaded to a dictionary for further processing and extraction of the necessary pieces of information.

For example, use the following code to print the description of the requested ticket:


.. code-block:: python

    import requests
    import json
    URL = "https://issues.apache.org/jira/rest/api/2/issue/ZOOKEEPER-2613"

    r = requests.get(URL)

    json_dict = r.json()

    print(json_dict['fields']['description'])



Language specific API wrappers
------------------------------------

As you could see in the previous examples, APIs can be accessed with any tool or language capable of sending HTTP requests.
However in most cases it is convenient to simplify the access to an API by encapsulating the operations in some language specific library.
That's why many APIs have their language specific wrappers that allow you to work on Objects and methods insted of raw HTTP requests.

There is a Python wrapper for JIRA REST API, named :py:mod:`jira`.

Install the module :py:mod:`jira` within your virtual environment (using PyCharm or in the command line using ``pip3 install jira``)


The analogous request for an issue, using the wrapper looks like so:

.. code-block:: python

    from jira import JIRA

    URL = "https://issues.apache.org/jira/"
    j = JIRA(URL)

    i = j.issue('ZOOKEEPER-2613')

    print(i.fields.description)


As you can see, the issue is an object, with fields corresponding to the sub-dictionaries of the original JSON response.
API wrappers offer many methods that significantly simplify the interaction with the API.


Excercise API00: Get a list of all issues from a JQL query
-----------------------------------------------------------

Use JIRA API wrapper to get a list of all issues from a JQL query (e.g. by issue type)

Tasks
++++++++

#. Check the documentation of :py:mod:`jira` to see how to execute a JQL query
#. Print the summaries of all found issues.


:ref:`API00_solution`

.. include:: track.rst