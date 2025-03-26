import math

#Circle
r = float(input("Enter the radius: "))
Circumference = 2 * math.pi * r
Area = math.pi * pow(r,2)
print(f"Circumference : {Circumference}\nArea : {Area}")

print()
#right angled triangle
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a,2)+ pow(b,2))
print(f"side c : {c : .2f} cm")