# JavaScript Object Notation

import json

people_string = '''
{
    "people":
    [
    {
        "name": "Aparna Shankar",
        "phone": "9895802537",
        "emails": ["aparna121@gmail.com", "aparnaspics@gmail.com"],
        "has_license" : true
    },
    {
        "name": "Abhishek Pednekar",
        "phone": "9845286737",
        "emails": null,
        "has_license" : true
    }
    ]
}
'''
# To load the string into a python Object

data = json.loads(people_string)
# print(type(data['people']))
# print(data)

for person in data['people']:
    print(person['name'])

for person in data['people']:
    del person['phone']

# To dump a json object into a python string

newstring = json.dumps(data, indent=2, sort_keys=True)  # indent argument helps in formatting the string in the form of a json, can also sort the keys
print(newstring)
