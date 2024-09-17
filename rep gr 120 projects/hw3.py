#Aiden Clarke 
#5/4/23
#hw3
#select problem number 
import math
gcn = 0
probnum = float(input("select a problem number 1-5 after a problem the program will jump to next problem:"))
if probnum == 1:

    #min/maz #1 
    minimum = float(input("give me two numbers and I will tell you info about it")) #input number   
    maximum = float(input("one more "))
        #min max less 
    if minimum == maximum:
                print("The two values are equal") 
                probnum =2
    elif maximum > minimum:
        print("The first number is the smaller number and the second number is the larger number ")
        probnum = 2
    elif minimum > maximum: 
        print("The first number is the larger number and the second number is the smaller number ")   
        probnum =2
print("end of question 1")
print("\n")    #problem 1
print("start of q2 ")






# problem number 2 
if probnum == 2:
#get number of sales 
    sales = float(input("how many sales where made"))
    bprice = 99.0
    if sales >= 100:
                discount = 0.5
    elif sales >= 50:
                discount = 0.4
    elif sales >= 20:
                discount = 0.3
    elif sales >= 10:
                discount =0.2
    else:
                discount = 0.0
            #calculate price
    total_cost = sales * bprice *(1-discount)
    print("total cost: $%.2f" % total_cost)
    probnum =3
print("\n")
print("end of q2"),print("start of q 3")
#problem 3 
if probnum == 3:
    print("now entering geometric calculation mode")
    print("1. calculate the area of a circle","\n""2.calculate the are of a rectangle","\n" "3. calculate the area of a triangle","\n","4.quit")
    gcn = float(input("what calculation do you want to do?"))
          # get info
if gcn==1:
    radius =float(input("what is the radius of the circle"))
    answer = math.pi * radius**2        #use info for math
    print("The area of the circle is: ", answer)
    print("end of q3"),print("\n"), 
    probnum=4
elif gcn == 2:                                        #next calculation same as first with different math but same input formula
    length= float(input("what is the length of the rectangle"))
    width = float(input("what is the width of the rectangle"))
    answer = length * width
    print(answer)
    print("end of q3"),print("\n") , 
    probnum=4

elif gcn == 3:
    base = float(input("what is the base of the trangle?"))
    hight = float(input("what is the hight of the triangle?"))
    answer = base * hight *0.5 
    print(answer)
    print("end of q3"),print("\n"),
    probnum=4

elif gcn == 4:
    print("end of question 3"),print("start of q ") ,print("\n"),
    probnum=4  

# start of questions 4 
if probnum == 4:
    print("thank you for choosing Serendipity Books sellers club")
    bb= int(input("How many books did you purchase this month"))
    if bb== 0:
        print("book bucks earned: 0"),("\n"),("end of q4 "),probnum == 5    # takes input and shows the number of book bucks earned 
    elif bb ==1:
        print("book bucks earned: 5"),("\n"),("end of q4 "),probnum == 5 
    elif bb ==2:
       print("book bucks earned: 15"),("\n"),("end of q4 "),probnum == 5
    elif bb ==3:
        print("book bucks earned: 30"),("\n"),("end of q4 "),probnum == 5
    elif bb >=4:
        print("book bucks earned: 60"),("\n"),("end of q4 "),probnum == 5
    #end of q 4
#end q 4 
probnum= 5


# This program practices if elif and else statements  
#from the door.py file 
if probnum==5:
    print("starting q 5")
    print ("You enter a dark room with two doors. Do you go through door #1 or\
    door #2? ")
door =float(input())                            #get info
if door == 1:                                    # info is checked for condition to tell the choice 
    print("There's a giant bear here eating a cheese cake. What do you do?")    
    print("""⠓⠒⠒⠉⣡⡤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⢾⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠄⠖⠛⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠈⠒⠒⠋⠁⡀⠀⠀⢀⣀⣀⠀⠀⠀⢀⣀⠤⠴⠒⠒⠚⠛⠓⠒⠒⠶⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠋⠀⠀⢈⡾⠉⠀⢀⡽⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⣴⡊⠉⠙⢢⡀⠀⠀⠀⠀⠈⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢧⣀⣠⢿⡁⣠⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠝⠢⡀⠀⡇⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢾⡁⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡄⢳⡀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⣀⣠⣤⣤⣴⣶⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⡷⠀⠀⠀⠀⠀⠀⠘⡄⢳⠀⠀⠀⠀⡇⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⡇⠀⠀⠀
⣿⡿⠿⠿⠿⠛⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⠀⠀⠀⠙⠿⢿⣿⣿⣿⣿⡿⠛⠀⠈⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⢀⡇⠀⠀⠀
⠁⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⢸⠁⠀⠀⠀
⡆⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⠀⠀⠀
⡇⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⢸⠀⠀⠀⠀
⣇⠀⠀⠀⢴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠞⠁⠀⢠⠇⠈⣧⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⠀⠀⠀⠀
⡘⣧⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡆⠀⠀⠀
⠇⢹⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⢧⠀⡇⠀⠀⠀
⢠⣿⣀⣈⡇⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠈⠻⡇⠀⠀⠀
⡏⢿⠉⣽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠙⡄⠀⠀
⡇⠉⠁⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠴⠂⠀⠀⠀⠀⠀⠸⡀⢸⡀⠀
⢧⣄⣀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⢀⡞⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⡇⠀
⡀⠀⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⣠⠎⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠛⠒⠚⠓⠒⠒⠒⠲⠒⠒⠒⠲⠤⠤⠤⠤⠤⠤⠤⠼⠤⠶⠧⠤⠄⠒⠒⠒⠒⠒⠚⠂⠀⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠓⠒
⣤⣤⣶⣶⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⣶⣶⣶⣶⣶⢶⣶⣶⣾⣶⣶""")        
    print("1.Take the cheesecake.")
    print("2.Scream at the bear")
    bear= input()
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":                     # repeat for each option
        print("The bear is offended eats your legs off. Good job!")
    else:
        print("Good job,",bear," is probably better. bear run away")
elif door == 2:
    print(".You stare into the endless abyss at Cthulhu's retina.")
    print("""⠀⣀⡀⠀⠀⣀⣤⣶⣾⣿⣿⣷⣶⣤⣀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠜⠉⣿⡆⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢰⣿⠉⠃⠀⠀⠀⠀⠀
⠀⢀⣤⣴⣦⣄⣴⠟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⢻⣦⣠⣴⣦⣄⠀⠀
⠀⡞⠁⣠⣾⢿⣧⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣽⡿⣷⣄⠈⢷⠀
⠀⣠⣾⠟⠁⢸⣿⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣿⡇⠈⠻⣷⣄⠀
⣰⡿⠁⠀⢀⣾⣏⣾⣄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣰⣷⣹⣷⠀⠀⠈⢿⣆
⣿⡇⠀⢠⣾⠏⢸⣿⣿⣿⣿⠋⢻⣿⣿⣿⣿⡟⠙⣿⣿⣿⣿⡇⠹⣷⡀⠀⢸⣿
⠹⣿⣴⡿⠋⠀⠈⠛⠉⣹⣿⣦⣄⡹⣿⣿⣋⣠⣶⣿⣏⠉⠛⠁⠀⠙⢿⣦⣿⠏
⠀⣸⣿⠿⠿⣿⣾⣿⡿⠿⣿⣿⣿⣿⡆⢰⣿⣿⣿⣿⠿⢿⣿⣶⣿⠿⠿⣻⣇⠀
⠀⣿⡇⢀⣴⣶⣤⣀⣴⣿⠿⣻⡿⣿⣧⣾⣿⢿⣟⠿⣿⣦⣀⣤⣶⣦⠀⢸⣿⠀
⠀⢿⣧⠈⠃⢀⣵⣿⡋⠁⢀⣿⡷⣿⡇⢻⣿⣿⣿⡀⠈⢛⣿⣮⡀⠘⠀⣼⡟⠀
⠀⠈⠻⣷⣤⣟⣋⣿⣧⣴⡿⠋⠀⣿⡇⢸⣿⠀⠙⢿⣦⣼⣿⣙⣻⣤⣾⠟⠁⠀
⠀⠀⠀⠈⢽⣿⠛⢻⣏⢉⣤⣶⣶⣿⠁⠈⣿⣶⣶⣤⡉⣽⡟⠛⣿⡏⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠿⣷⣾⣾⣟⣉⣠⣿⢿⡇⢸⠿⣿⣄⣙⣻⣷⣷⣾⠿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠛⢁⡼⠃⠘⢦⡈⠛⠿⠟⠃⠀⠀""")
    print("1.Blueberries")
    print("2. Yellow jacket clothespin")
    print("3.understanding revolver yellow melodies")
    insanity = input()
    if insanity == "1"or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    elif insanity == "3":
        print("the insanity rots your eyes in to a poll of muck. Good Job")
    else:
        print("you stumble around an fall on a knife and die. good job")
input("this has been HW 3 press enter to exit")