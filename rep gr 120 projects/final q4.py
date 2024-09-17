#Aiden Clarke 
#6/15/23
#final q4 



# Final - The area of a rectangle
# Write the getLength, getWidth, getArea,
# and displayData functions
def getLength():
    length = float(input("Enter Length: "))
    return length
def getWidth ():
    width=float (input ("enter Width:"))
    return width

    #gets the calues from the user and retuns them to main
def getArea(length,width):
    area=(length*width)
    return area      #calculates the area 
def displayData(length,width,area):
    print(f"The area of the rectangle of {length}l and {width}w is {area} ")
                            #^^^ displays the area using an f sting 







def main():
# Get the rectangle's length.
    length = getLength()
# Get the rectangle's width.
    width = getWidth()
    if width <0 or length <0:
        print("error input cant be negative")
        main()  #recalls main in values are negive
#get the rectangle's area.
    area = getArea(width,length)

#Display the rectangle's data.
    displayData(length, width, area)
    input()#calls display


main()