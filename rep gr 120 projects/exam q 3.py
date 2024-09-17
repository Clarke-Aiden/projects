#Aiden Clarke
#5/9/23
#exam 1
import math
# get wight 
weight = float(input("how much do you weigh in pounds?"))
# get hight
height = float(input("how tall are you in inches?"))
# calculate bmi 
bmi = round(weight * 703/(height*height),2)
#check wether optimal underwight or over weight.
if bmi >= 18.5 and bmi <=25:
    print("your BMI is optimal")
elif bmi < 18.5:
    print("you are underweight")
elif bmi > 25:
    print("you are overweight")
print(bmi)
input("press enter to exit")
