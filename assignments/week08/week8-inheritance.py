""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def get_info(self):
        return f"brand : {self.brand},model : {self.model},year : {self.year}"

class car(Vehicle):
    def __init__(self, brand, model, year,door):
        super().__init__(brand, model, year)
        self.door=door
    def get_info(self):
        return f"brand : {self.brand},model : {self.model},year : {self.year},door :{self.door}" 

mycar=car("hodna","kaba","2023",4)
print(mycar.get_info)