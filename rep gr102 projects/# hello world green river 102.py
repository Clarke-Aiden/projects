# hello world green river 102 
#aiden Clarke 10/7/23
import random 

#ask user for name 
def name():
    name = input("what is your name? ")
    return name 

#get name 
def age():
    global age
    age = int(input('how old are you '))
    return age

def afflist():
    list =['You are worthy of love and respect.',"You are capable of achieving your goals.","You are strong and resilient.","You are making a difference in the world.",'You are loved for who you are.','I believe in you.','You are capable of great things.','You are stronger than you think.','You are worthy of happiness and success.','You are not alone.','I am here for you.']
    global aff
    aff= random.choice(list)
    return aff 

#main controller 
def main():
    name()
    print("Nice to meet you ")
    age()
    print("Here is you affirmation for the day:")
    afflist()
    print(aff)
    yesno = str(input("do you want to know you are in x years?"))
    if yesno == 'yes' or 'y' :
        years = int(input("How many years fo you want to calculate?"))
        totalage = age + years
        print ("you will be ",totalage,"in", years, "years.")
        repeat()
    else: repeat()
         


def repeat():
    repeat=str(input("Do you want this program to repeat?"))
    if repeat == 'yes' or 'y':
         main()
    else:
     
        exit()


main()
