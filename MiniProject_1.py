#ASSIGNEMET 1 : SIMPLE LOGIN OR REGISTRATION FORM IN PYTHON 
print("-----WELCOME TO THE LOGIN PAGE MENU -----")
Registered = False
while True:
    print("\n1. REGISTER")
    print("2. LOGIN")
    print("3. FORGOT PASSWORD / PASSKEY")
    print("4. EXIT") 
    choice = input("ENTER YOUR CHOICE (1 TO 4):")
    if choice == "1":
        if Registered:
            print("YOU  ARE ALREADY REGISTERED ; NO NEED TO REGISTER ONCE AGAIN")
        else:
            Name = input("Enter your name :")
            Email = input("Enter your correct email address:")
            Address = input("Enter your current living address:")
            Phone_Number = input("Enter the correct phone number (10 digits ):")
            if len(Phone_Number) == 10 and Phone_Number.isdigit():
                Password = input("Enter your password / passkey (min 8 characters long):")
                if len(Password)>=8:
                    Registered=True
                    print(" YOU HAVE SUCCEESSFULLY REGISTERED ! ")
                else:
                    print(" PASSWORD / PASSKEY MUST BE ATLEAST 8 CHARACTERS LONG ")
            else:
                print(" PHONE NUMBER SHOULD BE OF 10 DIGITS AND OF NUMERIC DATATYPE")
    elif choice == "2":
        if not Registered:
            print("YOU ARE NOT REGISTERED , PLEASE DO REGISTER FIRST TO LOGIN ")
        else:
            L_Email = input("Enter your correct email address:")
            L_Password = input("Enter your password / passkey (min 8 characters long):")
            if L_Email == Email and L_Password == Password:
                print(" YOU ARE LOGGED IN ; LOGIN SUCCESSFUL ! ")
                print("WELCOME BACK",Name)
                print("Email Address: ",Email)
                print("Current living address: ",Address)
                print("Phone number: ",Phone_Number)

            else:
                print(" INVALID EMAIL OR PASSWORD ; PLEASE ENTER THE CORRECT DETAILS ")
    elif choice == "3" :
        if not Registered: 
            print("YOU ARE NOT REGISTERED , PLEASE DO REGISTER FIRST TO LOGIN ")
        else:
            L_Email = input("Enter your correct email address:")
            if L_Email == Email:
                New_Password = input("Enter the new password / passkey (min 8 characters long) ")
                if len(New_Password)>=8:
                    Password = New_Password
                    print(" PASSWORD / PASSKEY RESET SUCCESSFULLY ! ")
                else:
                    print(" PASSWORD / PASSKEY MUST BE ATLEAST 8 CHARACTERS LONG ")
            else:
                print(" EMAIL NOT FOUND ; PLEASE ENTER THE CORRECT EMAIL ")
    elif choice == "4":
        print(" GOODBYE !")
        break
    else:
        print(" INVALID CHOICE INPUT ; PLEASE ENTER A VALID INPUT (1 TO 4)")        