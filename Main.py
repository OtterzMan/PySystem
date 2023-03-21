import sys
import random
#####################################################################################################
def menu():
    print("""
----------
   MENU
----------
[1] Register
[2] Login
[3] Delete All DATA
    """)
    menuchoice = int(input("Choice:"))
    if menuchoice == 1:
        register()
    if menuchoice == 2:
        login()
    if menuchoice == 3:
        delete_data()
#####################################################################################################
def login():
            print("""
--------------------
       LOGIN
--------------------
[1] Username
[2] Password
        """)
            userin = input("Username:")
            try:
                f=open(f"data/{userin.lower()}.txt", "r", encoding="utf-8")
            except FileNotFoundError:
                print("Invalid Username")
                login()
            contents = f.read()
            usercheck = ""
            key = 48
            

            if usercheck == usercheck:
                passin = input("Password:")
                f=open(f"data/{userin.lower()}.txt", "r", encoding="utf-8")
                contents = f.read()
                passcheck = ""
                key = 48


                for a in contents:
                    x = ((((ord(a) - 10) // 13) -5000) - key)
                    x = chr(x)
                    passcheck += x

                if passcheck == passin:
                    print(f"""
    --------------------
          WELCOME
    --------------------
    Welcome Back {userin}.
                    """)
                    # Display basic user information
                    print("Here is some basic information about you:")
                    print("Username: " + userin)
                    print("Age: 25")
                    print("Gender: Male")
                    print("Email: example@gmail.com")
                    # Choose a welcome message randomly
                    welcome_messages = [
                        "It's great to see you again!",
                        "Welcome back! How was your day?",
                        "Hello again! How can I assist you today?",
                        "Nice to have you back! Ready for some fun?",
                        "Hey there! What brings you here today?"
                    ]
                    print(random.choice(welcome_messages))

                    print("""
------------------------
[1] Back to Menu
[2] Exit
------------------------
                    """)
                    loginchoice = int(input("Choice:"))
                    if loginchoice == 1:
                        menu()
                    elif loginchoice == 2:
                        exit()
                else:
                    print("Password Incorrect")
                    login()
#####################################################################################################
def register():
        print("""
--------------------
      REGSITER
--------------------
[1] Username
[2] Password
[3] Password Confirmation
        """)
        print("------------------------------")
        username = input("Username:")
        key = 48

        print("------------------------------")
        password = input("Password:")
        passwordconf = input("Confirm Password:")
        passout = ""
        if password == passwordconf:
            for a in passwordconf:
                x = (((ord(a) + key + 5000) * 13) +10)
                #if x < 1200000
                x = chr(x)
                passout += x
                f = open(f"data/{username.lower()}.txt","w+", encoding="utf-8")
                f.write(passout)
                f.close()

            print("Password Stored And Encrypted.")
            print("------------------------------")
            print("""
------------------------------------
      REGISTRATION COMPLETE
------------------------------------
[1] Menu
[2] Login
[3] EXIT
            """)
            registerchoice = int(input("Choice:"))
            if registerchoice == 1:
                menu()
            elif registerchoice == 2:
                login()
            elif registerchoice == 3:
                exit()
#####################################################################################################
def delete_data():
    print("""
-------------------------
      DELETE ALL DATA
-------------------------
Are you sure you want to delete all data? This action cannot be undone.
[1] Yes
[2] No
    """)
#####################################################################################################
menu()
