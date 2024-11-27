# 1. write a program to read employee data from the keyword and print that data?
# Ans :
class Employee:
    def __init__(self):
        self.emp_id = input("Enter Employee ID: ")
        self.name = input("Enter Employee Name: ")
        self.age = input("Enter Employee Age: ")
        self.salary = input("Enter Employee Salary: ")
        self.married = input("Enter Employee married: ")

    def display(self):
        print("\nEmployee Details:")
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Married:", self.married)

emp = Employee()
emp.display() 