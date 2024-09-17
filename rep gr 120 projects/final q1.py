#Aiden Clarke 
#6/15/23
#final q 1 



def calculateRetail(whosalecost,markupparcent):
    markup = whosalecost *(markupparcent /100)
    retailprice= (whosalecost + markup )
    return round(retailprice ,2)


def main():
    #gets the input on markups and cost 
    markupparcent = float(input("What is the mark up percentage?:"))
    whosalecost = float(input("What is the whole sale cost?:"))
    #checks for negitive values
    if whosalecost < 0 or markupparcent < 0 :
        print("Please enter a non negative number")
        main() # calls the calculator function with arguments 
    retailprice = calculateRetail(whosalecost, markupparcent)
    print("The retail price is: $%2.f"% retailprice)
    main() #^prints the output and formats it to be in 2 decimals



main()