def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

number = return_number_value()
print(number)
print(number + 5)
print(return_number_value() + 10)

number = return_number_value()
print('my number is ' + number)

Traceback (most recent call last):
  File "test.py", line 2, in <module>
    print('my number is ' + number)
TypeError: cannot concatenate 'str' and 'int' objects

number = return_number_value()
print('my number is ', number)
print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))
