#TUPLE
'''
it is ordered collection of items that are immutable
- immutable nature (items can't be changed once assigned)
'''
empty_tupel = ()
emp_tup1 = tuple([1,2,3])
print(emp_tup1)

# acessing tuple elements
emp_tup1[0] # indexing 
emp_tup1[0:2]

# tuple operation
t1 =(1,1,1, 'shub', True)
t2 = (1,2,3)
print(t1+t2)
print(t1*3)

# tuple methods
print(t1.count(1)) # counts the item '1'
print(t1.index('shub')) # return first index 'shub'

# packing and unpacking tuple;
packed_tuple = 1, "shubham", True, 2 #Tuple packing means assigning multiple values to a single tuple.
print(packed_tuple)

a,b,c,d = packed_tuple # Tuple unpacking means extracting values from a tuple and assigning them to variables.
print(a)
print(b)
print(c)
print(d)

# nested tuple 
nested = ((1,2,3), ('a','b','c'), (True, False))
print(nested)