# A = p (1+r/100)^t

print()
p = 0
r = 0
t = 0

while True:
    p  = float(input("Enter the principle amount: "))
    if p<0:
        print("Principle can't be negative")
    else:
        break
while True:
    r = float(input("Enter the intrest rate : "))
    if r<0:
        print("intrest rate can't be negative")
    else:
        break   
while True:
    t  = int(input("Enter the time: "))
    if p<0:
        print("time can't be negative")
    else:
        break 

total = p * pow((1 + r/100),t)

print(f"Balance after {t} year/s : ${total:.2f}")
