#Aiden Clarke
#5/9/23
#exam 1

# set varable for all data 
pack_amin = 450 #pack a
pack_ap = 39.99
pack_a_adp =0.45

#pack b
pack_bmin = 900
pack_bp = 59.99
pack_b_adp = 0.40
#pack c
pack_c =69.99

#print the diffret pacage options 
print("Package A: For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute. \n Package B: For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.\n Package C: For $69.99 per month unlimited minutes provided. ")
pack = str(input("what package did you purchased? A B OR C"))#get purchase info
#get the min used by user 
minutes = float(input("How many minuets where used this month? if package c put 0 \n"))
# calculate the monthly bill 
if pack == "A" or "a":              
    if minutes <= pack_amin:    
        total_bill = pack_ap
    else:                                                      # for each subtraced aloted min by the used min to get actualy used min 
        addmin = minutes - pack_amin                            # then calculate any overages and set ti to total bill
        total_bill = pack_ap + (addmin*pack_a_adp)
elif pack == "B" or "b":
    if minutes <= pack_bmin:
        total_bill = pack_bp
    else:
        addmin = minutes - pack_bmin
        total_bill = pack_bp + (addmin*pack_b_adp)
elif pack == "c" or "c":
    total_bill = pack_c
else:
    print("invalid package please restart")
#give total bill 
print("Your total bill is $",total_bill)
input("press enter to exit")


