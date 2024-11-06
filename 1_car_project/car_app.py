from playsound import playsound

#! How to create Class and objects: 
class Car(): 
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
        self.wheels = 4

    def start_engine(self): 
        playsound('/home/shakib4011/PlayGround/Learn python /OOP/1_class/start.mp3')
        return (f"{self.color} {self.brand} Engine started")
    
    def horn(self):
        playsound('/home/shakib4011/PlayGround/Learn python /OOP/1_class/horn.mp3')


#!Class
car_of_shakib = Car('Black', 'BMW')
car_of_someone = Car('white', 'Honda Civic')
 #!Methods
print(car_of_shakib.start_engine())
# car_of_someone.start_engine()
car_of_shakib.horn()

