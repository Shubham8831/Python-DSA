#1 if statement
"evaluates condition and excutes block of code, if condition is true" 

age = 20
if age> 18:
    print("you can vote")



#2 else 
"if condition is false then execute this block of code"

if age> 18:
    print("you can vote")
else:
    print("you can't vote")



#3 elif
"check multiple conditions"

if age> 18:
    print("you can vote")
elif age< 18:
    print("bhagg bsdk")
else:
    print("you can't vote")


#4 Nested Conditional Statement
"placing one or more if, elif, else statements inside another if, elif, else"

age = 5
height = 10
if age > 18:
    if height > 8:
        print("you can go to ride")
    else: 
        print("you can't go for the ride")
else:
    print("better luck next year")