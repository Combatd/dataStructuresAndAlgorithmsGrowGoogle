"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head # track the current top node as the next element
        self.head = new_element # the new_element is assigned as top node

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head: # if the top node exists
            deleted_element = self.head # set the top node as deleted_element
            next_element = deleted_element.next # hold value of next_element after deleted_element
            self.head = next_element # set the next_element as the new top node
            return deleted_element # return the deleted_element

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element) # uses class method insert_first to append element

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first() # uses class method delete_first to delete the last element
        pass
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)