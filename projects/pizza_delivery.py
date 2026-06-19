print("welcome to Python Pizza delivery")
size=input("Enter size of pizza? S,M or L \n ")
paneer= input("Do you paneer on your pizza? Y or N\n")

extra= input("Do you want extra cheeze ? Y or N\n")
bill =0

if size == "S":
    bill+=100
elif size == "M":
    bill+=150
elif size == "L":
    bill+=200
else:
    print("You have typed wrong input")

if paneer =="Y":
    if size == "S":
        bill+=20
    else:
        bill+=50

if extra =="Y":
    bill+=15

print(f"Your total bill : ${bill}")