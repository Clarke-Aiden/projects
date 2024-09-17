#Aiden Clarke 
#5/2/23
#quiz 6 


#obtaining info
num1 = float(input('give me a number'))
num2 = float(input('give me another number'))
num3 = float(input('one more number'))
#elif logic 
if num1 > num2 and num1 > num3:
    print('num1 is the largest')
elif num2 > num3 and num2 > num1:
        print('num2 is the largest')
elif num3 > num2 and num3 > num1:
    print('num3 is the largest')

input("press enter to exit")

