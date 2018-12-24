
#Dictionary - key-value pairs

student = {'name': 'John', 'age': 25 , 'courses': ['Math', 'CompSci']}

age = student.pop('age')




#print(student.get('phone','Not Found'))
#print(student.values())
#print(age)

for key, value in student.items():
	print(key, value)