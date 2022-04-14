"""
This is re run of a subclasses for python
link
https://www.youtube.com/watch?v=RSl87lqOXDE
"""
class Employee:
    raise_amt= 1.04
    
    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.email= first+ '.' + last+ '@gmail.com'
        self.pay= pay
        
    def fullname(self):
        return '{} {} '.format(self.first, self.last)
        
    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amt)
        
        
class Developer(Employee):
#we are simply inheriting from the Employee class all of its functionality
    
    raise_amt= 1.10
    
#    SO the user can put the language that they use
    def __init__(self, first, last, pay, prog_lang):
#        we are goign to knit method so we don't have to copy and paste code

        super().__init__(first, last, pay)
        self.prog_lang= prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees= None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees= []
        else:
            self.employees= employees
#    this is if we watn to add employees to the dictionary/ list of employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
# this is if we want to remove employees from the dictionary/ list of employees.
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())

dev_1= Developer('Corey', 'Shafer', 50000, 'Python')
dev_2= Developer('Test', 'Employee', 60000, 'C++')

mgr_1= Manager('Sue', 'Smith', 90000, [dev_1])
#print(mgr_1.email)
##now we are going to be adding more employees under the supervision of managager sue
#mgr_1.add_emp(dev_2)
#mgr_1.print_emps()
#
##now we are going to be removing an employee that is under the supervision of Sue
#print("We are going to remove one employee, employees remaining: ")
#mgr_1.remove_emp(dev_1)
#mgr_1.print_emps()


"""
Now we are going to be learning about two built in functions
instance()
"""
#this basically checks if what is in the parenthesis is occuring in the code or that i sin the peice of code
#meaning there is a person who is manager.

print(isinstance(mgr_1, Manager))

"""
Now we are going to be looking over the function that allows to see if there is a subclass that comes from a class
"""

#print(issubclass(mgr_1, Developer))
#this would return false

#this would come up as true
print(issubclass(Manager, Employee))
#print(dev_1.email)
#print(dev_1.prog_lang)
##
#print(dev_1.pay) #the original pay
#dev_1.apply_raise() #applying the raise
#print(dev_1.pay) #the new amount that the developer makes

#print(dev_1.email)
#print(dev_2.email)
