class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def info(self):
        print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")

# employee Instances. 
e1 = Employee("Mateo", 38, "developer", 200)
e2 = Employee("Sam Panda", 30, "developer", 100)
print(e1.name)
print(e2.age)
print("increment the Salary")
e1.increase_salary(10)
e2.increase_salary(20)
e1.info()
e2.info()


