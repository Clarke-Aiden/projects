#Aiden Clarke
#5/9/23
#exam 1

#get day from user 
day = int(input("what is day's date you would like me to use?"))
#get month 
month = int(input("what is the month you would like me to use?"))
#get year 
year = int(input("what is the last two digits you the year that you would like me to use?"))
#compute if month *day = year
if month * day == year:
    print("that date is magic")
else:                  #if the month does not == year print 
    print("that date is not magic") 
input("press enter to exit")      #safe exit