#Aiden Clarke 
#6/15/23
#final q 2

#takes the stepping input and uses it to caluclate for time using grav constant 
def falling_distance(i):
    g = 9.8
    t = i
    # calculates the distance
    distance =  round(0.5 * g*t**2,2)
    return distance
#^^ retuns the value to be printed 

def main(): 
    #makes table
    print("t(s)\td(m)\n------------------")
    for i in range(0,11):
        d= falling_distance(i) #for each i in range prints the value of i in the functuon  
        print(i, "\t",d)


main()
