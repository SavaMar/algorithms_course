from linked_list import LinkedList
from element import Element

# def main():
el1 = Element(11)
el2 = Element(22)
el3 = Element(33)
el4 = Element(44)
el5 = Element(55)
el6 = Element(66)
el7 = Element(77)
el8 = Element(88)
el9 = Element(99)


ll = LinkedList(el1)
ll.appendd(el2)
ll.appendd(el3)
ll.appendd(el4)
ll.appendd(el5)
ll.appendd(el6)
ll.appendd(el7)
ll.appendd(el8)
ll.appendd(el9)
print(ll.get_all_nodes())

# main()