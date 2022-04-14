"""

lecture from
https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5
"""
#student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
#
#print(student)# This will print all of the abov e
#
##this will pring only the name of the student
#
#print(student['name'])
#
##this will print the courses that the student has taken
#print(student['courses'])
#
##if we try to search something that is not in the dictionary then we will get an arror message
#
#print(student.get('name'))
##this will return the name of the studnet, this is calling by the value
#
#
##this will return none becasue we have not placed any phone number for the individual
#print(student.get('phone'))
##none is the default value
#
##however lets say that we want to change the default error message
#
#print(student.get('phone', '_Not Found_'))

#
#student['phone']= '555-555-5555'
##this is the new entry, but lets say that we want to change what is already in the dictionary, like the name
#
#student['name']= 'jane'
#print(student)


#however, we can also change all of this in oneline

#student.update({'name': 'Jane', 'age': 26, 'phone': '555-555-5555'})
#print(student) #prints the updated dictionary

#we can also delete elements from the dictionary
#del student['age']
#print(student)


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

#how to see what keys from the dictionary
print(student.keys())
"""
Will look something like this:
dict_keys(['name', 'age', 'courses'])
"""

#now to see the values
print(student.values())

#to see key and value pairs
print(student.items())

#to get the key values one by one

for key in student:
    print(key)

#to see the items from the dictionary
for key, value in student.items():
    print(key, value)
