#functions homw work 5
#Aiden clarke
#6/623


def half():
    print("Question 1")
    print("Half")
    print("Num \t Half-Num\n--------------")
    for num in range(1,11):
        print(num, "\t", num/2)
    main()

def timesTen():
    print("Times Ten")
    ans= ttn * 10
    print(ans)
    main()

def outpatient(hcs,hmc):
    total_charge = hcs + hmc
    print("The total charge for the out patient is ",total_charge)
    main()

def inpatient(hnday,hdr,hmc,hct):
    total_charge = hnday * hdr + hmc + hct
    print("The to total charge for the hospital stay is ", total_charge)
    main()

def main():
    print("Welcome to homework 5 please Question a number 1-3")
    global main_input
    main_input = int(input())
    if main_input == 1:
        half()
    elif main_input == 2:
        global ttn 
        ttn = int(input("give me a number to multiply by 10"))
        timesTen()
    elif main_input ==3:
        print("hospital stay calculator\n---------------------")
        print("Select wether the patient was a in-patient or an out-patient \n \t 1:in-patient \t 2:out-patient")
        hosp =int(input())
        if hosp == 1:
            print("some more data is to be collected")
            hnday = int(input("How may days where spent in the hospital?"))
            while hnday <1:
                    hnday = int(input("Invalid data entrey must be positive please renter"))
            hdr = int(input("What is the daily rate of the hospital?"))
            while hdr <1:
                    hdr = int(input("Invalid data entrey must be positive please renter"))
            hmc = int(input("what are the medication charges?"))
            while hmc <1:
                    hmc = int(input("Invalid data entrey must be positive please renter"))
            hct = int(input("charges for hospital tests ,etc?"))
            while hct <1:
                    hct = int(input("Invalid data entrey must be positive please renter"))
            inpatient(hnday,hdr,hmc,hct)
        elif hosp ==2: 
            print("some more data is required")
            hcs = int(input("What are the charges for the hospital services?"))
            hmc = int(input("What are the medication charges "))
            outpatient( hcs, hmc)

    else:
        print("Not a valid selection please try again")
        main()
    

main()


