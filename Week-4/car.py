class car :
    def __init__ (self ,model , make , year_of man):
        self.model = model 
        self.make = make
        self.year_of_manufacture = year_of_manufacture
#getters        
    def get_model(self):
        return self.model        
    def get_make(self):
        return self.make 
    def get_year(self):
        return self.year_of_manufacture
 #


car1 = car("demio" , "Nissan", 2006)
car2 = car("Hilux","Toyota" ,2004)

print(car1.get_model())
print(car1.get_model())
print(car1.get_year_of_manufacture())

