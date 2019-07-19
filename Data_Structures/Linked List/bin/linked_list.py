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
			
	def get_all_nodes(self):
		a = []
		current = self.head
		while current.next:
			a.append(current.value)
			current = current.next
		a.append(current.value)
		return a

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
		while i < position - 1:
			current = current.next
			i += 1
		previous_el = current.next
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

	def reverse_list(self):
		prev = None
		current = self.head
		next_node = current.next

		while next_node:
			current.next = prev
			prev = current
			current = next_node
			next_node = current.next

		self.head = current
		current.next = prev

	def is_element(self, x):
		current = self.head
		while current:
			if current.value == x:
				return True
			current = current.next
		return False

	def middle_node(self):
		slow = fast = self.head
		fast = slow.next
		while fast and fast.next:
			slow = slow.next
			fast = slow.next.next
		return slow

	def isalindrome(self):
		current = self.head
		a = ""
		while current:
			a += current.value
			current = current.next
		if len(a) % 2 != 0:
			return False
		return a == a[::-1]



# if __name__ == "__main__":
#     el1 = Element(11)
#     el2 = Element(22)
#     el3 = Element(33)
#     el4 = Element(44)
#     el5 = Element(55)
#     el6 = Element(66)

#     ll = LinkedList(el1)
#     ll.append(el2)
#     ll.append(el3)
#     ll.append(el4)
#     ll.append(el5)
#     ll.append(el6)
