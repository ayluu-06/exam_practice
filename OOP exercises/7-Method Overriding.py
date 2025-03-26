#!/usr/bin/python3


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee's name: {self.name}, Salary: {self.salary}"
    
class Manager(Employee):
    def __init__(self, name, salary, position):
        super().__init__(name, salary) #tiene que ser la funcion __init__
        self.position = position

    def get_details(self):
        base_details = super().get_details() #llama a la clase base y agrega info adicional
        return f"{base_details} Position: {self.position}"
    
employee1 = Employee("Juan", 15000) # no te olvides de la COMA aylincita :')  !!!!!
manager1 = Manager("Luna", 30000, "Manager") #agrega la posicion

print(employee1.get_details())
print(manager1.get_details())