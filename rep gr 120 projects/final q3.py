#Aiden Clarke 
#6/15/23
#final q3
import math
#^imports maths for squrt root

def findtiranglearea( a, b ,c):
    #takes value of a b c as arguments passed from main
    s = (a +b+ c)/ 2
    #creates the value of s 
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    #set area to  Heron's function 
    return round(area,2)
#retune ^^^ area as a round number 
def main():
    a = float(input("enter the length of side a :"))
    b = float(input("enter the length of side b: "))
    c = float(input("enter the length of side c: "))
    #^^^^ gives the values from user input for each side 
    if a < 0 or b < 0 or c <0 :
        print("please enter a length non negative")
        main()
        #recalls main if the values are negeitve 
    area =findtiranglearea(a, b, c)
    print(f"The area of that triangle is {area}",)
# gets the area from the function and prints it using an f sting 
main()