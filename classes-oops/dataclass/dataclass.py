'''
has a relationship

Employee has a project
'''
from dataclasses import dataclass


@dataclass(slots=True)
class Project:
    name: str
    duration: int
    technologies: list[str]

class Employee:
    def __init__(self, name, age, position, salary, project):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.project = project

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
    
    def __repr__(self):
        print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}. Employee is working on {self.project.name} project and involved technologies are {self.project.technologies}")

project1 = Project("E-commerce", 6, ["python", "django"])
project2 = Project("Healthcare", 12, ["java", "spring"])
employee1 = Employee("Mateo", 38, "developer", 200, project1)
employee2 = Employee("Sam Panda", 30, "developer", 100, project2)
employee1.increase_salary(10)
employee2.increase_salary(20)
employee1.__repr__()
employee2.__repr__()
