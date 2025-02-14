'''                                         CLASS
Class : it is description of object.
class has properties and functions(in python both are refered as attribute)
- it defines various attributes of an object
-> defining a class is creating a data type

    class -> common noun (i.e. doctor)
    object -> proper noun (i.e. doctor shubham)
    
object is something which is capable to store its properties and is capable to perform certain number of actions 
Encapsulation: act of combining properties and methods related to same object is known as encapsulation
ex - ramesh.running
       |       |
    object    action function

    all the variables(values/ properties it can store) and fn.(methods) will be in group in class
    so, class is a way to implement encapsulation
'''

'''

# ATTRIBUTES - attributes are member variables and member functions
    class test:
        x=5
        def f1():
            # some code
{[("x and f1 are attributes")]}


# OBJECTS - object is an instance of a class (way to represent real world entity)
    -> objects are of 2 types:

        ~ class object[one class has exactly one class object] but can have any number of instance object
        ex: class TEST
            TEST -> we represent its reference (class object)
            TEST() -> we represent its function call(make object and return its reference)

                variables made inside class object [class object variables](static variables)(common noun)

        ~ instance object  (t1 and t2 are instance object of test class)
                variables inside instance object [instance object variables](proper noun)


                    class test:
                        x = 5    #class object variable
                        def f1():
                            #code

                    t1 = test()
                    t2 = test()
       
         #to make instance onject variable : __init__() Method will be automatically be called each time we make object
'''
#1 
class test:
    def __init__(self):
        self.a=1
        self.b=2
t1= test()
t2= test()
print(t1.a, t1.b)
print(t2.a, t2.b)

#2
class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
t1= test(1,2)
t2= test(5,6)
print(t1.a, t1.b)
print(t2.a, t2.b)

'''
# METHODS 
    - instance method (to do instance specific task) min. one argument
    - static method (use @staticmethod decorator) either you give or not give argument
    - object method (use @classmethod decorator) 1 argument is passed 
'''
class test:
    x=5
    def __init__(self,a,b):    #instance method
        self.a=a
        self.b=b

    def show(self):            #instance method
        print(t1.a, t1.b)
    
    @staticmethod # no implicit argument is passed (no object and no class specific task)
    def f2():
        print("hello")

    @classmethod   # to access class members
    def f3(cls):
        print(cls.x)

t1= test(1,2)
t1.show()

test.f3()

test.f2()
t1.f2()


# create a class employee with attributes empid, name, salary and also define methods to access properties of employee
class employee:
    def __init__(self, id = None, name = None, salary = None):
        self.empid = id
        self.name = name
        self.salary = salary

    def setEmpid(self,id):
        self.empid =id

    def setName(self, name):
        self.name = name
    
    def setSalary(self,salary):
        self.salary = salary

    def getEmpData(self):
        print(f"id: {self.empid}, name: {self.name} and salary: {self.salary}")

e1 = employee()    
e2 = employee(1, "bobby", 25000)
e1.setEmpid(2)
e1.setName("billu")
e1.setSalary(50000)
e1.getEmpData()
