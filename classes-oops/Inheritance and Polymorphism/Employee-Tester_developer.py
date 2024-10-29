'''
this is a simple example of inheritance and polymorphism
is-a relationship

Developer is a Employee
Tester is a Employee

'''
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        if self.programming_language == "python":
            self.salary += bonus
class Tester(Employee):
    def __init__(self, name, age, salary, tools):
        super().__init__(name, age, salary)
        self.tools = tools

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        if "selenium" in self.tools:
            self.salary += bonus

employee1 = Developer("Mateo", 38, 200, "python")
employee2 = Tester("Sam Panda", 30, 100, ["selenium", "appium"])
employee3 = Developer("John", 40, 300, "java")
print("employee1 Details")
print(employee1.name)
print("Increment the Salary")
employee1.increase_salary(10, 100)
print(employee1.salary)

print("====================================")
print("employee2 Details")
print(employee2.name)
print("Increment the Salary")
employee2.increase_salary(10, 100)
print(employee2.salary)

print("====================================")
print("employee3 Details")
print(employee3.name)
print("Increment the Salary")
employee3.increase_salary(10)
print(employee3.salary)


