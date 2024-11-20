import datetime
now = datetime.datetime.now()
today = datetime.date.today()

print("Welcome to the Python PlainShell!")
print("Python PlainShell is similar to Microsoft Command Prompt, except it is based on Python and has minimal commands.")
print("Check the README that was with this for a list of commands!")
while True:
    command = input("Please enter a command:")
    if command == "specs":
        print("Operation Name: Python PlainShell")
        print("Base: 64-bit Python 3.9.0")
        print("Preferred Environment: Windows Visual Studio Code")
    elif command == "time":
        print(now.strftime("%I:%M:%S %p"))
    elif command == "date":
        print(today)
    elif command == "calcuate":
        operation_type = input("Please select a mathematical operation to calcuate; input must be in all caps: ")
        if operation_type == "ADDITION":
            print("You are now doing addition.")
            first_addend = int(input("Please input the first addend: "))
            second_addend = int(input("Please input the second addend: "))
            print("Okay, here is the answer!")
            print(first_addend+second_addend)
        elif operation_type == "SUBTRACTION":
            print("You are now doing subtraction.")
            minuend = int(input("Please input the minuend: "))
            subtrahend = int(input("Please input the subtrahend: "))
            print("Okay, here is the answer!")
            print(minuend-subtrahend)
        elif operation_type == "MULTIPLICATION":
            print("You are now doing multiplication.")
            first_factor = int(input("Please input the first factor: "))
            second_factor = int(input("Please input the second factor: "))
            print("Okay, here is the answer!")
            print(first_factor*second_factor)
        elif operation_type == "DIVISION":
            print("You are now doing division.")
            dividend = int(input("Please input the dividend: "))
            divisor = int(input("Please input the divisor: "))
            print("Okay, here is the answer!")
            print(dividend/divisor)
        else:
            print("Sorry, that is an invalid mathematical operation!")
    elif command == "quit":
        break
    else:
        print(str({command}) + "was not recognized as a valid command.")