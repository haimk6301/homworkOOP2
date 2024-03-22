class Employee:

    def __init__(self, name, surname, experience, salary, address, monthly_salary, role):
        self.__name = name
        self.__surname = surname
        self.__experience = experience
        self.__salary = salary
        self.__address = address
        self.__monthly_salary = monthly_salary
        self.__role = role
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, experience):
        self.__experience = experience

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        self.__monthly_salary = monthly_salary

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    def get_monthly_salary(self):
        return self.__monthly_salary

    def __calculate_bonus(self):
        return self.__role.monthly_salary_factor * self.__monthly_salary

    def get_bonus(self):
        bonus = self.__calculate_bonus()
        print(f'{self.name} you got {bonus} as the annual bonus')
        return bonus

    def print_employee(self):
        print(f"Name: {self.__name} {self.__surname}")
        print(f"Experience: {self.__experience} years")
        print(f"Salary: {self.__salary}")
        print(f"Address: {self.__address}")
        print(f"Monthly Salary: {self.__monthly_salary}")
        print(f"Role: {self.__role.name}")
        print(f"Description: {self.__role.description}")

    def promote_employee(self, new_role):
        self.__role = new_role
        self.__monthly_salary = new_role.monthly_salary_factor * self.__monthly_salary
        self.__salary = self.__monthly_salary * 12



