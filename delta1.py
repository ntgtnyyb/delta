import random as r
import time as t

def commands():
    print("0 - functions ")
    print("1 - about module delta ")
    while True:
        try:
            inp = int(input("Enter number that is equal to question: "))
            if inp == 0:
                print("1. plus = x + y")
                print("2. minus = x - y")
                print("3. divide = x ÷ y")
                print("4. multiply = x × y")
                print("5. degree = x^y")
                print("6. minmult = (x - y) × x")
                print("7. pludiv = (x + y) ÷ x")
                print("8. x2 = x × 2")
                print("9. randomf: This is function that select random numbers and random function")
                print("then you need to input in brackets max number that function can select")
                print("and then he prints 1th number, 2nd number and function ")
                print("10. timer: simple timer where you need to input in brakets time")
                break
            elif inp == 1:
                print("delta is module with functions that make you code faster to make")
                break
        except ValueError:
            print("Input valid number")
def plus(x,y):
    print(x+y)
def minus(x,y):
    print(x - y)
def divide(x, y):
    print(x/y)
def multiply(x,y):
    print(x*y)
def degree(x, y):
    print(x**y)
def minmult(x, y):
    print((x - y)*x)
def pludiv(x,y):
    print((x + y)/x)
def randomf(x):
    r1 = r.randint(0, x)
    r2 = r.randint(0, x)
    r3 = r.randint(1,7)
    if r3 == 1:
        print("x is: ", r1)
        print("y is:", r2)
        print("function is: plus")
        plus(r1, r2)
        return ""
    elif r3 == 2:
        print("x is: ", r1)
        print("y is:", r2)
        print("function is: minus")
        minus(r1, r2)
        return ""
    elif r3 == 3:
        print("x is: ", r1)
        print("y is:", r2)
        print("function is: divide")
        divide(r1, r2)
        return ""
    elif r3 == 4:
        print("x is: ", r1)
        print("y is:", r2)
        print("function is: multiply")
        multiply(r1, r2)
        return ""
    elif r3 == 5:
        print("x is: ", r1)
        print("y is:", r2)
        print("function is: degree")
        degree(r1, r2)
        return ""
    elif r3 == 6:
        print("x is: ", r1)
        print("y is:", r2)
        print("function is: minmult")
        minmult(r1, r2)
        return ""
    elif r3 == 7:
        print("x is: ", r1)
        print("y is:", r2)
        print("function is: pludiv")
        pludiv(r1, r2)
        return ""
def timer(x):
    while True:
        print(x)
        x = x - 1
        t.sleep(0.9)
        if x < 0:
            print("Time out")
            break
def x2(x):
    print(x*2)