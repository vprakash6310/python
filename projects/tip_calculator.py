
print("Welcome to the Tip Calculator! ")
bill=float(input("What was the total bill?"))
tip=int(input("what percent tip would you like to give? 10,12 or 15 ,20?"))
n=int(input("How many people to split the bill ?"))
tip_percent=tip/100
total_tip=bill*tip_percent
total_bill =bill + total_tip
total_per_person=total_bill/n
Final = round(total_per_person,2)
print(f"Each person should pay : {Final}")


