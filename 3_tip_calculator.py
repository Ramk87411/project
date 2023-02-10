print("Welcome to the tip calculator")
bill = float(input("what was the total bill? "))
tip = float(input("what is the bill tip %:"))
per_bill = tip/100
# print(per_bill)
person = int(input("How any pepole to split the bill? "))

total_bill = bill+(bill*per_bill)

each_person_bill = (total_bill /person)
print("Each person should pay " , round(each_person_bill,2))