from posixpath import split


print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
spit = input("How many people to split the bill? ")

total_bill_float = float(total_bill)
tip_float = float(tip) / 100 + 1
split_float = float(spit)

final_bill_individual = total_bill_float * tip_float / split_float

print(f"Each person should pay: $ {round(final_bill_individual,2)} ")
