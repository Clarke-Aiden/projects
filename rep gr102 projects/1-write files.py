#10/21/23
#aiden clarke
#write files
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
f=open (dir_path +"/Hackme.txt","w")

name = str(input("what is you name?"))
color= str(input('what is your fav color'))
petn = str(input('What was your frist pet name?'))
mothermadinname= str(input('what is your mothers madian name?'))
elms = str(input('what elementary School did you attend'))

with open("Hackme.txt",'w') as f:

    f.write(name + '\n')
    f.write(color +'\n')
    f.write(petn +'\n')
    f.write(mothermadinname +'\n')
    f.write(elms +'\n')



