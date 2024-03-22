class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_yearly_expenses(self):
        total_expenses = 0
        for employee in self.employees:
            yearly_expense = employee.monthly_salary * 12 + employee.get_bonus()
            total_expenses += yearly_expense
        return total_expenses


