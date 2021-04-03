#Employee: Write a class called Employee. The __init__() method should take in a first
#name, a last name, and an annual salary, and store each of these as attributes. Write a method
#called give_raise() that adds $5,000 to the annual salary by default but also accepts a different
#raise amount.
#Write a test case for Employee. Write two test methods, test_give_default_raise() andtest_give_custom_raise(). Use the setUp() method so you don’t have to create a new
#employee instance in each test method. Run your test case, and make sure both tests pass.

class Employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    
    def describe_employee(self):
        return(f"{self.firstname.title()} {self.lastname.title()} ${self.salary}")
    
    def give_raise(self, amount=5000):
        self.salary += str(amount)
        return(f"{self.firstname.title()} {self.lastname.title()} just got a {amount} payrise.")
        


#my_emp = Employee('ben', 'holla', 100000)
#my_emp.describe_employee()
#my_emp.give_raise()
#my_emp.describe_employee()
#my_emp.give_raise(10000)
#my_emp.describe_employee()

employo = Employee('ben', 'holla', '100000')
employo.describe_employee()
employo.give_raise()
employo.describe_employee()