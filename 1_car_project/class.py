class Employee: 
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    #!Instance method
    def display(self):
        print(self.name, self.id)
    
emp1 = Employee("John", 11)
emp1.display()
emp2 = Employee("David", 12)
emp2.display()