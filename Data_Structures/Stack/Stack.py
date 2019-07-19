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

    def get_position(self, position):
      if position < 1:
        return None
      
      current = self.head
      if position == 1:
        return current
      i = 1
      while i < position:
        current = current.next
        i += 1
      return current

    def insert_first(self, new_element):
      new_element.next = self.head
      self.head = new_element

        

    def delete_first(self):
        if self.head:
            current = self.head
            self.head = current.next
            return current
        else:
            return None


class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
print(ll.delete_first().value)
print("position 1: ",ll.get_position(1).value)
print("position 2: ",ll.get_position(2).value)

# ll.insert_first(33)
# print("position 1: ",ll.get_position(1).value)
# print("position 2: ",ll.get_position(2).value)
# print("position 3: ",ll.get_position(3).value)
# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
# print stack.pop().value
# print stack.pop().value
# print stack.pop()
# stack.push(e4)
# print stack.pop().value