class Node:
    def __init__(self, element):
        self.element = element
        self.next=None
        
class CircularLinkedList:
    def __init__(self):
        self.head=Node('head')
        self.head.next=self.head
        self.current=self.head
        
    def show(self):
        cur_node=self.head
        while cur_node.next.element != 'head':
            print(cur_node.element, end=' -> ')
            cur_node=cur_node.next
        print(cur_node.element)
        
    def insert(self, new):
        new_node=Node(new)
        new_node.next=self.head
        self.current.next=new_node
        self.current=new_node
        
    def find_next(self, n):
        for _ in range(n):
            if self.current.next.element == 'head':
                self.current=self.current.next
            self.current=self.current.next
    
    def remove(self, node):
        prev_node=self.head
        while prev_node.next != node:
            prev_node=prev_node.next
        prev_node.next=prev_node.next.next
        
def Josephus(m,n):
    a=CircularLinkedList()
    for i in range(1,n+1):
        a.insert(i)
        
    for _ in range(n-2):
        a.find_next(m)
        a.remove(a.current)
    a.show()
    
        