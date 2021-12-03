class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.previous = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = Node('head')
    
    def show(self):
        cur_node = self.head
        while cur_node.next is not None:
            print(cur_node.element, end=' -> ')
            cur_node = cur_node.next
        print(cur_node.element)
        
    def insert(self, item, new):
        new_node = Node(new)
        cur_node = self.find(item)
        next_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next = new_node
        new_node.previous = cur_node
        if next_node is not None:
            next_node.previous = new_node
        
        
    def find(self, item):
        cur_node = self.head
        while cur_node.element != item:
            cur_node = cur_node.next
        return cur_node
    
    def remove(self, item):
        cur_node = self.find(item)
        cur_node.previous.next = cur_node.next
        if cur_node.next is not None:
            cur_node.next.previous=cur_node.previous
            cur_node.next = None
        cur_node.previous=None
        
    def find_last(self):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        return cur_node
    
    def show_reverse(self):
        cur_node = self.find_last()
        while cur_node.previous is not None:
            print(cur_node.element, end=' <- ')
            cur_node = cur_node.previous
        print(cur_node.element)