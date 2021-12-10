class Stack:
    def __init__(self):
        self.data=[]
        
    def push(self, element):
        self.data.append(element)
        
    def pop(self):
        return self.data.pop()
    
    def length(delf):
        return len(self.data)
    
    def show(self):
        print(self.data)
        
    def clear(self):
        self.data.clear()
        
