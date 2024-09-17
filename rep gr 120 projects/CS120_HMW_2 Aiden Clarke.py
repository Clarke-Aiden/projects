# CS120_HMW_2 Part II_Program Challenge
# Insert your name and time finished below

# Name:Aiden Clarke 
# Time finished:4/20/23

# Work directly on this .py with your answer.
import math
"""In this homework you're going to
         ***name variables*** and work with simple math
Comment your code as necessary
Submit your .py file on CANVAS before due date

"""

print("Problem 1") # (5 pt)

"""If a 2000 pound pregnant hippo gives birth to a 100 pound calf,
but then eats 50 pounds of food, how much does she weigh?"""

# Write your code
x = 2000
y = 100
z = 50
x1 = 1900
print("If a 2000 pound pregnant hippo gives birth to a 100 pound calf, but then eats 50 pounds of food, how much does she weigh")
print("x =2000","y=100" ,"z=50")
print("x-y=",x-y ,"x1+z=",x1+z)
print(z) #answer

print("""----End of Problem 1 ----- """)
input("Press any key to continue")

print("Probelm 2") # (5 pt)

"""

If you run a 10-kilometer race in 43 minutes 30 seconds,
what is your average time per mile?
What is your average speed in miles per hour?
(Hint: there are 1.61 kilometers in a mile).

"""

# Write your code
rl= 10
t= float(43.5)
kim= 1.61
rlm= round(10/1.61,8)
prm = t//rlm 
print("If you run a 10-kilometer race in 43 minutes 30 seconds,what is your average time per mile?","\n"  "What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).")
print("ten kilometer in miles 10/1.61=", rlm)
print("43.5 minutes divided by 6.21371192 miles is", t / rlm ,"per mile")
print("60min per hour divided by 7 comes to ", round(60/7,2) ,"miles per hour")







print("""----End of Problem 2----- """)
input("Press any key to continue")

print("Probelm 3") #(5 pt)

''' If the two sides of a right triangle are known:
a = 134 cm, b = 165 cm,
calculate the length of the hypotenuse c.
Your anwer should be displayed with correct unit. '''

#write your code
a=134
b=162
c= (a**2)+(b**2)
z= int(math.sqrt(c))
print("f the two sides of a right triangle are known:a = 134 cm, b = 165 cm, calculate the length of the hypotenuse c.""\n""Your anwer should be displayed with correct unit. '")
print("a**2+b**2=",c)
print("sqr(44200)=", int(math.sqrt(c)))
print(z,"cm")



print("""----End of Problem 3----- """)
input("Press any key to continue")


print("Probelm 4") #(5 pt)

'''Write a program that computes the total sales tax on a $128 purchase.
Assume that state sales tax is 4% and the county sales tax is 2%.   '''


#write your code
p=128
st= 4
ct=2
tt=st+ct
salestax=7.68
print("Write a program that computes the total sales tax on a $128 purchase","\n","assume that state tax is %4 and the county sales is 2%")
print("total tax is equal to state tax + county tax =",st+ct)
print("sales tax is calculated by multiplying purchase total by tax rate.",p*tt)
print(salestax+p)










print("""----End of Homework 1----- """)
input("Press any key to Exit")
