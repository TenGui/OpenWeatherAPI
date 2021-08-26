import todoist
import sys
import os
sys.path.append(os.getcwd())
sys.path.append('../')
from privatekeys.api_keys import apikeys

api = todoist.TodoistAPI(apikeys['todoistpersonalkey'])
api.sync()
full_name = api.state['user']['full_name']
print(full_name)

for things in api.state['items']:
    print(things)