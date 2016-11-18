from sphinx.ext.intersphinx import fetch_inventory
import warnings
from pprint import pprint as print

uri = 'https://jira.readthedocs.io/en/master/'

# Read inventory into a dictionnary
inv = fetch_inventory(warnings, uri, uri + 'objects.inv')

print(inv)

task_details = {'project': 'LSYPA',
                'summary': 'Task summary',
                'description': 'Task description',
                'issuetype': {'name':'Task'}
                }

j.create_issue(project='LSYPA', summary='New Task summary',
               descryption='Description of the new task',
               issuetype={'name':'Task'})