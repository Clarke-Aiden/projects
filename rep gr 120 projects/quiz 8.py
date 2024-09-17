#Aiden Clarke
#5/11/23
#quiz 8 keeping a running total

print("Hello Teacher ")
total = 0
student_completed = 0
running_total = input("what was you score on the test out of 100?\n")
while student_completed <= 7:
    total = total + int(running_total)
    student_completed +=1
    running_total = input("what did the next student get on the test out of 100?\n")
    print("the number of student that have completed are",student_completed)
print("the total score of the student is",total)
print("the average score of the student is",total/student_completed,"\nhave a good day")
input("press enter to exit")