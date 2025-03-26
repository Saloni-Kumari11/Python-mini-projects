def calculate_bill(amount):
    if amount<800:
        return amount
    elif 800<=amount<1200:
        tax= 0.10 * amount
        return amount +tax
    elif 1200<=amount<2000:
        tax= 0.15 * amount
        return amount +tax
    else:
        tax= 0.22 * amount
        return amount +tax
    

bill_amount = float(input("Enter the electric bill amount: "))
total_bill = calculate_bill(bill_amount)
print(f"The total bill amount with tax is : {total_bill:.2f}")