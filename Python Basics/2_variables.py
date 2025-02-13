'''
# name convwention:
    - descriptive name
    - start with letter or _
    - variables are case senstitive
'''

age = 12
print("age: ", age)


'''
Python is dynamically typed -> type of variable is determined at runtime

'''

# type checking
print(type(age))


# type conversion
age_str = str(age)
print(type(age_str))


# dynamic typing
var = 10
var ='abc'
var = 2.5
print(type(var))


# Input funtion: 
age = input("enter your age: ") # type -> string

age = int(input("enter your age : "))

