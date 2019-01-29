import json


 # load the JSON file into a python object
# file_dict = open('States.json','r')
# data = json.load(file_dict)
# file_dict.close()

with open('States.json', 'r') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

for state in data['states']:
    del(state['area_codes'])

# Dump the python object into a file

with open('New_states.json', 'w') as f:
    json.dump(data, f, indent=2)
