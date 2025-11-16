def divide(divideBy):
    try:
        return 42/divideBy
    except :
        print("error: you tried to divide by zero")

divide(0)

a=input("enter an integer")
try:
    if int(a)>3:
        print("bapre 3?")
    print("letitbe")
except ValueError:
    print("value should be integer")

