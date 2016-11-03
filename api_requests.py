
def get_description_with_requests():
    import requests
    import json
    URL = "https://issues.apache.org/jira/rest/api/2/issue/ZOOKEEPER-2613"

    r = requests.get(URL)

    json_dict = r.json() # normal python dictionary
    return json_dict['fields']['description']
    #print(json.dumps(json_dict, indent=3)) # to pretty-print



from jira import JIRA

URL = "https://issues.apache.org/jira/"
j = JIRA(URL)

search_results = j.search_issues('type="New Feature"', maxResults=100)
for issue in search_results:
    print(issue.fields.summary)