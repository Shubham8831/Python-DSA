# ASSIGNMENT NUMBER - 3 

#1 Define a class node to describe a node of a singly linked list.
class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next


#2 define a class sll to implement singly linkedlist with __init__() method to create and initilise start reference variable.
class SLL:
    def __init__(self, start=None):  # None means no item in linkedlist
        self.start = start


#3 define a method is_empty() to check if the linked list is empty in sll class
    def is_empty(self):
        return self.start == None


#4 in class sll define a method insert_at_start() to insert an element at the starting of the list
    def insert_at_start(self, data):
        n = Node(data,self.start)    # make node first item has data and next has next node ref. (always first put data in node) 
        self.start = n #put value of n new object in start


#5(imp.) in class sll define a method insert_at_last() to insert an element at the end of the list
    def insert_at_last(self,data):
        n = Node(data)  # make node and give data, next will have None
        if not self.is_empty():
            temp = self.start # we make a temp variable and put the first node ref. in it
            while temp.next is not None:
                temp = temp.next        # temp will have the ref. of next node
            temp.next  = n # we put ref. of new node in last node next
        else: # if list is empty
            self.start = n

#6 in class sll define a method search() to find the node with specified element value
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp # reference of node we are searching for 
            temp = temp.next
        return None # element not found

        

#7 in class sll define a method insert_after() to insert a new node after a given node of the list
    def insert_after(self,node,item):
        if node.search():

#8 In class SLL, define a method to print all the elements of the list.
    def print_(self):
        for nodes in Node.instance:
            print(f{nodes.item})


#9 In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
#10 In class SLL, define a method delete_first() to delete first element from the list.
#11 In class SLL, define a method delete_last() to delete last element from the list.
#12 In class SLL, define a method delete_item() to delete specified element from the list.