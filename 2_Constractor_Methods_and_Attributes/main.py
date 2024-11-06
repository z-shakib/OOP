class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #! method to display greeting message: 
    def greet(self): 
        print(f"Hello, My name is {self.name} and I am {self.age} Years Old.")

    #! method to upgrade person age: 
    def set_age(self, new_age):
        self.age = new_age
        print(f"{self.name}'s age has been updated to {self.age}")
    
#! Create an object (instance) of the person class:
person_1 = Person("shakib", 22)
# print(person_1)

#! Call greet method: 
person_1.greet()

#! Update the age using set_age method: 
person_1.set_age(33)

#! Call greet method again to check updated information: 
person_1.greet()

