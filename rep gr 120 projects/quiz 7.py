# Aiden Clarke 
# 5/11/23
#quiz 7 
#loops 

number = 2          # even numbers loop 
while number <= 100:       #if number is less then 100 loop and add to number 
    print(number)
    number += 2

#security program but with loops 
#demostate if else loops 
print ("Welcome to System Security Inc.")
print("--- where secutiy is our middle name\n")
password = input("Enter you password.\n")
while password != "secret":
    print("Password denied. Please try again ")
    password = input("Enter you password.\n")
else:
    print("Access Granted")
input("\n\n press enter to exit")