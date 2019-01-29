"""
Java Script Object Notation

* JSON is similar to a dictionary in Python
* However, JSON is actually a string. it can be stored in .txt files whose contents are read as a string
* JSON requires 'key-values' to be enclosed in double quotes and nor single quotes unlike dictionaries
*
"""

import json

people_string = '''
{
    "people": [
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

''' To convert a string into a Python Object i.e a dictionary, we use loads() '''

# Here data is the dictionary, 'people' is the key and the data['people'] is the list that
# forms the value of this key
# To access each member of the list, you can use the list index

data = json.loads(people_string)
print(type(data['people']))
print(data['people'][1])

# Now, you can access the elements of the list. Here, person is the first element of the list, which is a dictionary
# therefore, to access the value inside this dictionary, you will have to use the key
# person['name']

# for person in data['people']:
#     print(person['name'])

data['people'][1]['emails'] = ['abhi_ap@yahoo.com']
print(data['people'][1]['emails'])

# for person in data['people']:
#     del person['phone']


''' To dump a JSON object (python dictionary) into a python string(or JSON file), we use dumps() '''

newstring = json.dumps(data, indent=2, sort_keys=True)  # indent argument helps in formatting the string in the form of a json, can also sort the keys
print(newstring)

# In the above, data was a dictionary created by loading a JSON. We can also dump a python dictionary
# into a file and it will automatically create a JSON (with double quotes)

cars = [
    {
        'make': 'Ford',
        'model': 'Ikon'
    },
    {
        'make': 'Honda',
        'model': 'City'
    }
]

with open('Cars.txt','w') as wr_file:
    cars_string = json.dump(cars, wr_file)
print(cars_string)


