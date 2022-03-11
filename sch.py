
def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete existing Student")
        print("4. Delete existing Student")
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

def home():
    while 1:
        print("welcome to the college system")
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
            auth_admin()
        else:
            print("No valid option was selected")

home()