'''                                                       ARRAY


# how to make array in python?  ->  using numpy library(not in builtin types)

# array : basic data structure, it is collection of similary type of items , elements are indexed(stored sequentially), its size is fixed

# python has built-in module called as builtins. [int, float, str, list, tuple, dict, set, range, bytes, objects, exception]
{python has module called array.py}

# fixed size array not present in builtin python, array is not a bulit-in data structure and therefore needs to be imported

# array are sequence type and behave very much like list but array can have elements of limited types.

from array import *
a1 = array(type code, [elemets])

type code:
'b' signed integer
'B' unsigned integer
'u' unicode character
'h' signed integer
'H' unsigned integer
'i' signed integers
.
.
.
'''

from array import *
a1 = array('i', [1,2,3])
print(a1)
print(a1[0])       # indexing
print(type(a1))

for x in a1:
    print(x+5)


''' 
# Array Methods : [append(), count, extend, fromlist, insert, pop(index), remove(value), reverse, tolist]
'''
a1.append(4)
print(a1)

a1.reverse()
print(a1)

a1.pop()
print(a1)




'''                                                           LIST

- list is a class (in builtins)
- list is mutable(changeable)
- list element are indexed
- list is iterable
- list can contain diffferent type element
- list can grow ( coz it is implemented through : dynamic array)



                                                    array vs dynamic array

array : 
    - collection of same type elements
    - fixed size
    - indexed

dynamic array:
    - collection of same type elements
    - resizable ( size not fixed)
    - indexed
'''
l0 = []        #list
l1 = [1,2,3]
l2 = [1, 1.2, 'abc']

#in python array and list are not of fixed length, but in general programming array are of fixedsize
'''
# List Methods : [append, clear, count, extend, index, insert, pop, remove, sort, reverse]
'''

'''
# Builtin Methods in Python : [len(), sum, max, min, sort]
'''


# list and array both are growable in python
# list can contain heterogeneous data
# array can contain homogeneous data


'''                                                    NUMPY
if you want to perform mathematical calculation, then you should use numpy array by importing numpy package.
otherwise use list as it work in a similar way and more flexible to work with. 

- use numpy for fixed length array
- pip install numpy (in cmd/terminal)
'''
import numpy as np
a = np.array([1,2,3])
print(a)

b = np.array([[1,2,3],[4,5,6]]) # 2d array 
c = np.array([[10, 20, 30], [5, 6]]) # 1d array with two list type elements




# ASSIGNMENT - 1
# Given an array with some integer type values. Write a python script to sort array values?
array1 = array('i', [5,2,1])
print(array1)
array1 = sorted(array1)
print(array1)

# Given a list of heterogeneous elements. Write a python script to remove all the non-int values from the list.
list2 = [1, 2, 2.5, 'True', 'shubham']
for i in list2:
    if type(i) != int:
        list2.remove(i)
print("list2: ", list2)

# Write a Python script to calculate average of elements of a list.
list1 = [1,2,3]
print(len(list1))
avg = sum(list1)/len(list1)
print(avg)

# Write a Python script to create a list of first N prime numbers.
def is_prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
def prime_list(N):
    num=2
    p = []
    while len(p)<N:
        if is_prime(num):
            p.append(num)
        num+=1
    return p
    
N = int(input("Enter the value of N: "))
print("First", N, "prime numbers:", prime_list(N))

# Write a Python script to create a list of first N terms of a Fibonacci series.
def fib(n):
    if n==0:
        return []
    elif n==1:
        return [0]
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[-1]+fib[-2])

    return fib
n = int(input("Enter the value of N: "))
print("First", n, "terms of Fibonacci series:", fib(n))