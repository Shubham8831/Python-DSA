# LIST 
'''
- ordered and mutable(changed) collection of items
- can contain items of different data type
'''
# creating list
lst = []
lst1 = ['shub', 25, True]
lst2 = ['a', 'b', 'c','d', 'e']
# acessing items in the list  
print(lst2[1] )# by indexing 
print(lst2[-1])
print(lst2[1:])
print(lst2[0:2])

# modifing list elements
lst2[0] = 'z'
print(lst2)

#list methods

lst2.append("f") # add item at the end
lst2.insert(0,'a') # add item at specific index
print(lst2)
lst2.remove("z") # remove first occourance of item (take item name)
print(lst2)
lst2.pop(0) # remove last item or item at sepecific index
print(lst2)
print(lst2.index("c")) # gives index of the item
print(lst2.count('d')) # gives count of the items
lst3 = ['z', 'a', 'f', 'm', 'y']
lst4 = [True, False] #f:0,t:1
lst4.sort() # sorts the item in ascending order
print(lst4)
lst3.reverse(  ) # reverse the list
print(lst3)
lst3.clear() # removes all the items from the list

lst5 = ['a', 'b', 'c','d', 'e']
lst5.sort(reverse=True) # to sort in descending order
print(lst5)

#slicing list
print(lst5[::2]) # start end gap
print(lst5[3:]) # 3 to end
print(lst5[:2]) # start to 1 (index)

# iterate over list
for i in lst5:
    print(i)

# iterating with index
for index,letter in enumerate(lst5):
    print(f"index: {index} and item: {letter}")

#list comprehension  [operation output]
square = [x**2 for x in range(10)]
    # expression  #item   # iterable
print(square)

# list comprehension with conditional logic [expression for item in iterable if condition]
even = [num for num in range(10) if num%2==0]
print(even)

# nested list comprehension
# [expresseion for item1 in iterable1 for item2 in iterable2]
l1 = [1,2,3]
l2 = ['a', 'b','c']
pair = [(i,j) for i in l1 for j in l2 ]
print(pair)