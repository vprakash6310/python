import random
letters=['A','B','C','D','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
number=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*']

print("Welcome to PY Password Generator!")
n_letter=int(input("Enter number of letters in your password:\n"))
n_number=int(input(f"Enter number of numbers in your password:\n"))
n_symbol=int(input(f"Enter number of symbols in your password:\n"))

#password = ""
#for i in range(0,n_letter):
#   password += random.choice(letters)

#for i in range(0,n_symbol):
#   password+=random.choice(symbols)
#for i in range(0,n_number):
#   password+=random.choice(number)
#print(password)

#Hard version
password_list=[]
for i in range(0,n_letter):
    password_list.append(random.choice(letters))
for i in range(0,n_number):
    password_list.append(random.choice(number))
for i in range(0,n_symbol):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)
password=''

for i in password_list:
    password += random.choice(letters)
print(f"your Password is : {password}")