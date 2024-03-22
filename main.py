import self

from model.Company import Company
from model.Employee import Employee
from model.Role import Role

if __name__ == '__main__':
    role1 = Role('Programmer', 'Writes Programs', 2)
    employee_1 = Employee('Yoram', 'Nagar', 14, 300000, 'Bialik 7', 25000, role1)

    print()
    employee_1.get_bonus()
    print()
    employee_1.print_employee()
    print()

    role2 = Role('Manager', 'Operation Manager', 2.5)
    employee_2 = Employee('Aharon', 'Kedmi', 22, 360000, 'hatkuma 30', 30000, role2)

    employee_2.get_bonus()
    print()
    employee_2.print_employee()
    print()

    new_role = Role('Team Leader', 'Leads Programing Team', 1.5)
    employee_1.promote_employee(new_role)

    print()
    print(f"{employee_1.name} this is your role and monthly salary after promotion:")
    print(employee_1.role.name)
    print(employee_1.monthly_salary)
    print()
    company = Company()
    company.add_employee(employee_1)
    company.add_employee(employee_2)
    for employee in company.employees:
        employee.print_employee()
        print()

    total_expenses = company.total_yearly_expenses()
    print("Total Yearly Expenses for the Company:", total_expenses)