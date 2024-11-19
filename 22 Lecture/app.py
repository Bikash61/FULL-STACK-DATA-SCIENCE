class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender
    def display(self):
        print(f'The name is {self.name} and age is {self.age} and gender is {self.gender}')

class Employee(People):
    def __init__(self, name, age, gender, employee_id, salary):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.salary = salary
        def display(self):
            super().display()
            print(f'The employee id is {self.employee_id} and salary is {self.salary}')

object1 = Employee("BIkas",12,"Male",121,1234)
object1.display()



