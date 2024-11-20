'''try:
    print("start code")
    print(10 / 0)
    print("no errors")
except NameError:
    print("we have an error")
except ZeroDivisionError:
    print("ZeroDivisionError")
    print("code after capsule")'''

'''try:
    print("start code")
    print(10 / 0)
    print("no errors")
except (NameError,ZeroDivisionError) as error:
    print("we have", error)

    print("code after capsule")'''

'''try:
    try:
        print("start code")
        print(error)
        print("No errors")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)'''

'''try:
    print("Hello")
    print(error)
    print("No error")
except NameError as error:
    print(error)
else:
    print("No problems")
finally:
    print("Finally code")'''

'''try:
    print("Hello")
     # print(error)
    print("No error")
except NameError as error:
    print(error)
else:
    print("No problems")
finally:
    print("Finally code")'''

try:
    x1 = int(input("number1"))
    x2 = int(input("number2"))
    print(x1+x2)
    print(x1-x2)
    print(x1/x2)
    print(x1*x2)
except ZeroDivisionError:
    print("Помилка: Ділення на нуль неможливе.")
except ValueError:
    print("Помилка: Введені дані не є числом.")