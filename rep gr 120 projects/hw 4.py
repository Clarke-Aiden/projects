#Aiden Clarke 
#5/23/23
#hw 4 

question_number = int(input("Please enter the question number you would like to jump to: "))


if question_number == 1  :     
    total = 0 
    count = 1 
    print("counting program")
    print("im going to as for 10 numbers and give you the total of them")
    while count <= 10:        #  ask for the number and set the increase the number amount 
        number = int(input("Enter number {}:" .format(count)))
        total += number 
        count += 1 
    print("The final total is :", total)
    question_number = 2

if question_number == 2:
    bugs_collected =0 
    total_bugs =0
    day = 1
    print("--bug collecting program--")
    for day in range(1,6):                        # set a range of the number of days to be one more than the number as it starts at 0 
        bugs_collected = int(input(f"Enter the number of bugs collected on day {day}:")) # get input for the number of bugs collected 
        while bugs_collected <0 :              #verify that the number collected is more then 0 
            print("you can collect a negative number of bugs!")
            bugs_collected = int(input(f"Enter the number of bugs collected on day {day}:"))        # use an f string to  add the number of days the sting 
        total_bugs += bugs_collected                                                                
    print("Total bugs collected:",total_bugs)     #print the number total number of bugs combine with the daily total
    question_number = 3

if question_number == 3:
    print("multiplcation program")
    q3number = int(input("Enter a number:"))
    for i in range(1,11):                                    # for the defined range * number by the input
        q3a = q3number * i                                   
        print(f"{q3number}x {i} = {q3a}")    
question_number=4               # print the formated sting including the resalting number 

if question_number == 4:
    q4even=0
    q4odd=0
    q4_range = [2,23,24,12,56,3,66,15,89,1,123,5,90]
    print("even and odd finder")
    print(q4_range)                                     # gets the range and checks the number by devideing it by 2 then desideds if its even or odd 
    for num in q4_range:
        if num % 2 == 0:
            print(num,"is even")
            q4even += 1
        else: 
            print(num,"is odd")
            q4odd += 1
    print("the total number of even numbers is", q4even)  #prints if even of odd and the total
    print ("the total number of odd number is ", q4odd)
question_number = 5

            
if question_number == 5:
    print("hours calc")
    employee_number=0
    employee_number =int(input("how many employees worked?:"))
    n_days = 0
    overall =0             #^sets var to be 0 for clean slate  
    for n in range(1,employee_number+1):    #gets number of employees
        total =0
        n_days = int(input(f"Enter the number of days worked by employee {n}:"))      #gets days for each emplyess
        for day in range(n_days):
            hrs = int(input("How many Hours did you work on day %d:" % (day+1)))         #  gets the hours for each days 
            while hrs > 8:                
                print("The maximum hours that you can work each day is 8.")        #verifys that hours are not over 8 if they are it aks for a re enter
                print("re-enter the number of hours on day %d:" %(day+1))            
                hrs = int(input("How many Hours did you work on day %d" % (day+1)))
            total += hrs
        print("Employee %d, your worked %d hours .\n" % (n,total))           #adds the total and then displays 
        overall +=total
    print("Total number of hours worked by %d employees are : %d" %(employee_number,overall))
1