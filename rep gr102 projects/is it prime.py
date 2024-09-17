# aiden Clarke
#10/25/2023
#is it prime
import math 

def get_input():
    global usernum
    usernum = int(input("Enter a number and ill tell if its prime or not.->"))
    return usernum

def is_it_prime():
    if usernum <= 1:
        print("Please enter a positive number.")
        main()
    for i in range(2, int(math.sqrt(usernum))+1):
        if usernum % i ==0:
            print(f"{usernum}:is not a prime number.")
            break
        else:
            print(f"{usernum}:is a prime number")
            break
            
    
def main():
    get_input()
    is_it_prime()
    main()


main()