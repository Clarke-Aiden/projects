# loop program 102 
#Aiden Clarke 10/11/23



def send_message():
    for i in range(10):
            print ("Yes it is.")

def main ():
    user_input = str(input("Is today a good day?"))

    if (user_input == "y"):
        send_message()
        main()    
    elif user_input == "n" or"N": 
        print ( "Yesterday is history and tomorrow is a mystery but to day is a gift, that is why it is called the present.") 
        return
        
       

    
    


main()












