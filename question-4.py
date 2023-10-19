score = input("Please type your exam score out of 100 here >>>")
score = int(score)
if score <= 49 :
    print ("Grade Awareded = U")
    print ("Would you like to book a retake?")
    retake = input("Would you like to retake the exam? Please answer Y or N>>>")
    if retake == 'Y':
        print ("Retake booked for tomorrow at 2pm")
    elif retake == 'N' :
         print ("You will need to book later")
    else:
        retake = input("Please answer Y or N>>>")
        if retake == 'Y':
            print ("Retake booked for tomorrow at 2pm")
        elif retake == 'N' :
             print ("You will need to book later")

            
             
elif score <= 59 :
    print ("Grade Awareded = D")
    print ("You achieved a Pass")

elif score <= 69 :
    print ("Grade Awareded = C")
    print ("Good effort")

elif score <= 79 :
    print ("Grade Awareded = B")
    print ("Very good")

else :
    print ("Grade Awareded = A")
    print ("Excellent result")

