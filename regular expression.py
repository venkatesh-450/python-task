def phone():
    length = len(phNo)
    if length == 12 and phNo[:3] == "+91" :
        print("Valid Phone Number")
    else :
        print("Invalid Phone Number")

phNo = input("Enter the phone number:")
phone()