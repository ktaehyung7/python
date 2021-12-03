class Node:
    def __init__(self, element):
        self.element = element
        self.next=None
        
    
class LinkedList:
    def __init__(self):
        self.head=Node('head')

    def show(self):
        cur_node=self.head
        while cur_node.next is not None:
            print(cur_node.element, end=' -> ')
            cur_node = cur_node.next
        print(cur_node.element)
        
    def find(self, item):
        cur_node=self.head
        while cur_node.element != item:
            cur_node = cur_node.next
        return cur_node
    
    def insert(self, current, new):
        new_node = Node(new)
        cur_node = self.find(current)
        new_node.next = cur_node.next
        cur_node.next = new_node
        
    def find_previous(self, item):
        cur_node=self.head
        while (cur_node.next is not None) and (cur_node.next.element != item):
            cur_node = cur_node.next
        return cur_node
    
    def remove(self, item):
        prev_node = self.find_previous(item)
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next
        