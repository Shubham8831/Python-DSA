# DICTIONARIES
'''
- unordered collection of items
- store data in key value pair
- key must be unique and immutable while value can be of any type
'''

# creating dict
dict1 ={}
dict2 = dict(name="John", age=25, city="New York")

# acessing dictionary element
dict2['age']
dict2.get('city', "not present") # it prints not present if key is not present in dict

# mofifying dictionary elements
dict2["name"] = "shubham" # updated the value of key
print(dict2)
dict2['add'] = 'alpha 1'  # added new key value

del dict2["name"] # delete key value pair

# dictionary method
dict2.keys() # get all the keys
dict2.values() # get all the values
dict2.items() # get all key value pairs

# shallow copy: this will allocate different memory
dict2_copy = dict2.copy()

# iterate over dic
for key, value in dict2.items():
    print(f"key : {key} value: {value}")

# nested dict
stu = {
    "stu1" : {"name": "shub", "age":25},
    "stu2" : {"name": "veddyaa", "age":5}
}
print(stu["stu1"]["age"])

# iteration over nested dict
for id, info in stu.items():
    for key, value in info.items():
        print(f"{key}, {value}")

# dict comprehension
dic5 = {x:x*2 for x in range(5)}
print(dic5)

# coditional dict comprehension
evens= {x:x*2 for x in range(11) if x%2==0}
print(evens)

# merge 2 dictionaries
d1 = {'a':1, 'b':2}
d2 = {'b':3, 'c':4}
d1_d2_merged = {**d1, **d2} #  merge two dictionaries in Python using dictionary unpacking (**).
print(d1_d2_merged)