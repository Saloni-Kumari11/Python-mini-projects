print()
weight = float(input("Enter weight : "))
unit = input("Kilogram or Pound ? (K or L): ")

if unit.upper() == "K":
    weight = weight * 2.205
    unit ="Lbs"
elif unit.upper() =="L":
    weight = weight / 2.205
    unit ="Kgs"
else :
    print(f"{unit} is not valid")        

print(f"Your weight is {round(weight)} {unit}")    