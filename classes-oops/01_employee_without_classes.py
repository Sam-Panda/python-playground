def init_employee(name, age, position, salary):
    return {
        "name": name,
        "age": age,
        "position": position,
        "salary": salary
    }

def increase_salary(employee, percent):
    employee['salary'] += employee['salary'] * (percent/100)

def employee_info(employee):
    print(f"{employee['name']} is {employee['age']} years old. Employee is a {employee['position']} with the salary of ${employee['salary']}")


employee1 = init_employee("Mateo", 38, "developer", 200)
print("Employee 1 details :: \n")
employee_info(employee1)
print("Employee 1 Details post Increment :: ")
print("\n")
increase_salary(employee1, 10)
employee_info(employee1)

increase_salary(employee1, 10)
employee_info(employee1)