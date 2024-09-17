#Aiden Clarke 
#6/1/23
# functions


def print_star():
    print("*********")

def print_message():
    print("How do you do ?")


print_star()
print_message()
print_star()

def main():
    print("Enter a number,I will tell is it is even or odd")
    usernum = int(input())
    iseven(usernum)

    
def iseven(usernum):
    if usernum % 2 == 0:
        print("The number is even")
    else:
            print("The number is odd")


main()