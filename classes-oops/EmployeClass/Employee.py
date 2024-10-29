class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = 0

    
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = salary
        # if we change the salary, we need to reset the annual salary
        self._annual_salary = None
    

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name should be a string")
        self._name = name
    

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age
    
    # computed property
    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self.salary * 12
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

employee1 = Employee("Mateo", 38, "developer", 200)
print(employee1.name)
print(employee1.age)
print("Increment Salary")
employee1.increase_salary(10)
print(employee1.salary)
print(" lets look at the annual salary")
print(employee1.annual_salary)
print("Increment Salary by 10 percent")
employee1.increase_salary(10)
# check if we set the annual salary to zero
# employee1.annual_salary = 0
print(employee1.annual_salary)