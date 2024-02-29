#!/usr/bin/env python3

def admin_login(username, password):
    return "Access granted" if (username == 'admin' or username == "ADMIN") and password == '12345' else "Access denied"
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    pass

def fizzbuzz(num):
    # your code here
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    # your code here
    operations = ['-', '+', '*', "/"]
    #python iterates through operations
    if operation not in operations:
        print ("Invalid operation!")
        return None
    answer = eval(f"{num1} {operation} {num2}")
    return answer
    pass
