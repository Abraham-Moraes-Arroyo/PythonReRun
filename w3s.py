#import array
#for name in array.__dict__:
#    print(name)


#This is an exmaple for classes OOP

class Employee:
    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first+ '.' + last+ '@companu.com'
    
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#based on what we put for the class, we then start to fill out the 'arguments of the code below
emp_1= Employee('abraham','morales', 50000)
emp_2= Employee('cas','marin', 60000)

#print(emp_2.fullname())
emp_1.fullname()
Employee.fullname(emp_1)
print(Employee.fullname(emp_1))


#print(emp_1.email)
#print(emp_2.email)
#print(emp_1)
#print(emp_2)
#these are the instances variables
#However all of this can be avoided if we create a class
#these are manual scripts
"""
emp_1.first= 'abraham'
emp_1.last= 'morales'
emp_1.email= 'abraham.morales@uic.edu'
emp_1.pay= 5000


emp_2.first= 'Cas'
emp_2.last= 'Marin'
emp_2.email= 'cas.marin@uci.edu'
emp_2.pay= 60000
"""
