#Employee: Write a class called Employee. The __init__() method should take in a first
#name, a last name, and an annual salary, and store each of these as attributes. Write a method
#called give_raise() that adds $5,000 to the annual salary by default but also accepts a different
#raise amount.
#Write a test case for Employee. Write two test methods, test_give_default_raise() andtest_give_custom_raise(). Use the setUp() method so you don’t have to create a new
#employee instance in each test method. Run your test case, and make sure both tests pass.
import unittest
from exercise import Employee

class TestEmployee(unittest.TestCase):

    def test_response_employee(self):
        employo = Employee('ben', 'holla', '100000')
        rar = employo.describe_employee()
        self.assertEqual(rar, 'Ben Holla $100000')

    def test_raise_employee(self):
        employrar = Employee('ben', 'holla', '100000')
        test = employrar.give_raise()
        self.assertEqual(test, 'Ben Holla just got a 5000 payrise.')

if __name__ == '__main__':
    unittest.main()


