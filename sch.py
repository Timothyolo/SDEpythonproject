import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="", database="college")
command_handler = db.cursor(buffered=True)

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
            print("Admin login")
        else:
            print("No valid option was selected")

home()