class Vehicle:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color

    def start_engine(self):
        return "Engine started"
    

class Car(Vehicle):
    
    def start_engine(self):
        return f"The car's engine from {self.brand} is now roaring."


class Motorcycle(Vehicle):
    def start_engine(self):
        return f"The motorcycle's engine from {self.brand} is now revving."



m = Vehicle("Civic", "Honda","Red")
a = Car("Audi-R8","Audi","Black")
b = Motorcycle("Air Blade","Honda","Black_White")
print(m.start_engine())
print(a.start_engine())
print(b.start_engine())
