#this is code from youtube upon Classes
# link
"""
https://www.youtube.com/watch?v=BJ-VvGyQxho
"""

"""
class Employee:
    num_of_emps= 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email = first + '.' + last +'@company.com'
    
    
        Employee.num_of_emps +=1 #here is where we will increement the count if there are new employees added
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amount)
    
emp_1= Employee('Abraham', 'Morales', 50000)
emp_2= Employee('Tona', 'Arroyo', 60000)

#print(Employee.__dict__)

#emp_1.raise_amount= 1.05

#print(Employee.raise_amount) #1.04
#print(emp_1.raise_amount) #1.05
#print(emp_2.raise_amount) #1.04
#

print(Employee.num_of_emps)

"""


"""
This is the third part of the video
"""

class Employee:
    num_of_emps= 0;
    raise_amt= 1.04
    
    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.email= first + '.' + last+ '@email.com'
        self.pay= pay
        
        Employee.num_of_emps +=1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amt)
        
#    class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt= amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay= emp_str.split('-')
        return cls(first, last, pay)
        
#   additiona constructors
    @classmethod
    def fromtimestamp(cls, t):
        """
        Construct a date froma POSIX timestamp
        (time.time())
        """
        y, m, d, hh, mm, ss, weekday, jday, dst= _time.localtime(t)
        return cls(y, m, d)
        
        
    @classmethod
    def today(cls):
    """Construct a data from time.time
        
emp_1= Employee('Corey', 'Moist', 5000)
emp_2= Employee('Lasslo', 'Monterrey', 6000)

#Employee.set_raise_amt(1.05)
#
#print(Employee.raise_amt)
#print(emp_1.raise_amt)
#print(emp_2.raise_amt)

#Using class methods as alternative constructors
emp_str_1= 'JQhn-Doe-70000'
emp_str_2= 'Steve-Smith-30000'
emp_str_3= 'Jane-Doe-90000'

new_emp_1= Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
