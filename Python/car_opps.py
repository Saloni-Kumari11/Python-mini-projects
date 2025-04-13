from car import Car

car1 = Car("Mustang",2024,"red",False)
car2 = Car("Corvette",2025,"blue",True )
car3 = Car("Charger",2026,"yellow",True)

print(car1.model)
print(car2.year)
print(car3.color)
print(car1.for_sale)

car1.drive()
car3.stop()

car1.describe()