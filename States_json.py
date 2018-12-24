import json


 # load the json file into a python object
with open('States.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

for state in data['states']:
    del(state['area_codes'])

# Dump the python object into a file

with open('New_states.json', 'w') as f:
    json.dump(data, f, indent=2)
