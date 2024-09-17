#Aiden Clarke
#5/9/23
#exam 1

# define max rage and min rage 

min_dis = 10 
max_dis = 3000

# get wight and distance 
weight = float(input("enter the weight of the package in kg :"))
if weight <= 0:
    print("invalid weight must be greater than 0 ")
elif weight > 20:
    print("invalid weight must be less than 20 ")
else:
    distance = float(input("what is the distance to be shipped in miles"))
    if distance < min_dis or distance > max_dis:
        print("invalid distance  ")
    else:
        if weight <= 2:
            rate = 1.10
        elif weight <= 6:
            rate = 2.20
        elif weight <= 10:
            rate = 3.70
        else:
            rate = 4.80
        shipingc = distance / 500 *rate
        print("the shiping cost is : ", shipingc)
        #ran out of time