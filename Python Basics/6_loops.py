#1 for loop -> [ iterate over sequence ]

name = "shubham"
for i in name:
    print(i)

for i in range(5):  # 0 -> 4
    print(i)

for i in range(1,6): # 1 -> 5
    print(i)

for i in range(1,11,2): # 2 is step size
    print(i)            # 1 3 5 7 9

for i in range(10,1,-2):
    print(i)            # 10 8 6 4 2



#2 while loop -> [ execute as long as condition is true ]

count = 0
while count<5:
    print(count)   # 0 1 2 3 4
    count +=1



# loop control statement -> [ break, continue, pass ]

''' 'break' = {'exits the loop permaturely(permanently)'} '''
for i in range(10):
    if i == 5:
        break
    print(i)

''' 'continue' = {'skips the current iteration and continue with the next'} '''
for i in range(10):
    if i ==5:
        continue
    print(i)

''' 'pass' = {'does nothing'} '''
for i in range(5):
    if i==3:
        pass 
    print(i+10)



# Nested Loop -> [ loop inside loop ]
for i in range(3):
    for j in range(2):
        print(f"i: {i} and j: {j}")

for num in range(1, 101):
    if num > 1:  # 1 is not a prime number
        for i in range(2, num):
            if num % i == 0:
                break  # Not a prime number
        else:
            print(num)  # Prints only if the loop wasn't broken (i.e., prime number)
