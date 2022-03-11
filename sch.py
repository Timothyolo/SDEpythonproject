#This is my main function with infinite loop
def home():
    while 1:
        print("welcome to the TLG bootcamp")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("Student login")
        elif user_option == "2":
            print("Teacher login")
        elif user_option == "3":
            auth_admin()  # Linked to the function decleared below once authenticated
        else:
            print("No valid option was selected")

# To authenticte a valid admin credentials.
def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("incorrect password !")
    else:
            print("Login details not recognised")

#These are what the admin can do while on session
def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete existing Student")
        print("4. Delete existing Teacher")
        print("5. Logout")

        user_option = input(str("option : "))
        if user_option == "1":
            print("")
            print("Register New Student")
            username = input(str("Student Username : "))
            password = input(str("Student password : "))
            query_vals = (username,password)
            
            print(username + " has been registered as a student")

        elif user_option == "2":
            print("")
            print("Register New Teacher")
            username = input(str("Teacher Username : "))
            password = input(str("Teacher password : "))
            query_vals = (username,password)
            
            print(username + " has been registered as a teacher")

        elif user_option == "3":
            print("")
            print("Delete Existing student Account")
            username = input(str("Student Username : "))
            query_vals = (username, "student")
            print(username + " has been deleted")
            
        elif user_option == "4":
            print("")
            print("Delete Existing Teacher Account")
            username = input(str("Teacher Username : "))
            query_vals = (username, "teacher")            
            print(username + " has been deleted") 
        
        elif user_option == "5":
            break
        else:
            print("you did not select a valid option")

home()