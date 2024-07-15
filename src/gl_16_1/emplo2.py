"""
Для класса Employee и Client, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""


class Employee:

    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):

        if isinstance(other, int):
            return self.pay + other
        if isinstance(other, self.__class__):
            return self.pay + other.pay
        return self.pay


class Client:

    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        return other


class Developer(Employee):
    pass


class Manager(Employee):
    pass


# код для проверки
users = [Employee(30000), Client(100000), Developer(60000), Manager(70000)]
# users = [Employee(50000), Manager(50000)]
total_salary = 0
for user in users:
    total_salary = user + total_salary

# for user in users:
#     if issubclass(user.__class__, Employee):
#         total_salary = user + total_salary

print(total_salary)


# Вывод: 150000


class Dividend:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other_investment):
        for e in other_investment:
            self.amount += e.amount
        return self.amount


investmentA = Dividend(150)
investmentB = Dividend(50)
investmentC = Dividend(25)

# print(investmentA + [investmentB]) #200
print((investmentA + [investmentB, investmentC]))


class Employee:
    first: str
    last: str
    pay: float

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.first}", "{self.last}", {self.pay})'

    def __str__(self):
        return f'{self.fullname} - {self.email}'

    def __len__(self):
        return len(self.fullname)

    # def __add__(self, other):
    #     return self.pay + other.pay

    def __add__(self, other):
        if isinstance(other, Employee):
            return Employee("", "", self.pay + other.pay)
        else:
            return other.pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'.lower()

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


class Employee2:
    first: str
    last: str
    pay: float

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


emp_1 = Employee("Petr", "Petrov", 25)
emp_2 = Employee("Ivan", "Ivanov", 80)
emp_3 = Employee("Gleb", "Glebov", 35)
emp_5 = Employee2("Gleb", "Glebov", 65)
sum_emp_pay = emp_2 + emp_3 + emp_1 + emp_3
sum2 = emp_1 + emp_5
print(sum_emp_pay.pay)
print(sum2)
