"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""
#  + get_lenght

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
  def __init__(self, head=None):
    self.head = head
  
  def append(self, new_node):
        if self.head:
      current = self.head
      while current.next != None:
        current = current.next
      current.next = new_node
    else:
      self.head = new_node

    #     def append(self, new_element):
#         current = self.head
#         if self.head:
#             while current.next:
#                 current = current.next
#             current.next = new_element
#         else:
#             self.head = new_element

  def get_position(self, position):
    if position < 1:
      return None
    current = self.head
    i = 1
    while i < position:
      current = current.next
      i += 1
    return current
  
  def insert(self, new_element, position):
    if position < 1:
      return None
    current = self.head
    i = 1
    while i < position-1:
      current = current.next
      i += 1
    previous_el = current.next
    print("previous_el", previous_el.value)
    current.next = new_element
    current.next.next = previous_el
  
  def delete(self, position):
    current = self.head
    i = 1
    if position == 1:
      self.head = current.next

    while i < position-1:
      current = current.next
      i += 1
    current.next = current.next.next

  def get_length(self):
    current = self.head
    length = 1
    while current.next:
      current = current.next
      length += 1
    return length


  
el1 = Element(11)
el2 = Element(22)
el3 = Element(33)
el4 = Element(44)


print(el1.value)
ll = LinkedList(el1)
print(ll.head.value)

ll.append(el2)
print(ll.head.next.value)

ll.append(el3)
print(ll.head.next.next.value)

print("position 1: ",ll.get_position(1).value)
print("position 2: ",ll.get_position(2).value)
print("position 3: ",ll.get_position(3).value)

ll.insert(el4,3)
print("insert ====================")
print("position 3: ",ll.get_position(3).value)
print("position 4: ",ll.get_position(4).value)

ll.delete(2)
print("delete ====================")
print("position 1: ",ll.get_position(1).value)
print("position 2: ",ll.get_position(2).value)

ll.delete(1)
print("delete ====================")
print("position 1: ",ll.get_position(1).value)
print("position 2: ",ll.get_position(2).value)


# ======= answer
# class Element(object):
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList(object):
#     def __init__(self, head=None):
#         self.head = head

#     def append(self, new_element):
#         current = self.head
#         if self.head:
#             while current.next:
#                 current = current.next
#             current.next = new_element
#         else:
#             self.head = new_element

#     def get_position(self, position):
#         counter = 1
#         current = self.head
#         if position < 1:
#             return None
#         while current and counter <= position:
#             if counter == position:
#                 return current
#             current = current.next
#             counter += 1
#         return None

#     def insert(self, new_element, position):
#         counter = 1
#         current = self.head
#         if position > 1:
#             while current and counter < position:
#                 if counter == position - 1:
#                     new_element.next = current.next
#                     current.next = new_element
#                 current = current.next
#                 counter += 1
#         elif position == 1:
#             new_element.next = self.head
#             self.head = new_element

#     def delete(self, value):
#         current = self.head
#         previous = None
#         while current.value != value and current.next:
#             previous = current
#             current = current.next
#         if current.value == value:
#             if previous:
#                 previous.next = current.next
#             else:
#                 self.head = current.next