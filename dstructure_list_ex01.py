class List:
    def __init__(self):
        self.list=[]
        self.pos=0
        self.size=0
        
    def append(self, element):
        self.list.append(element)
        self.size +=1
        
    def __len__(self):
        return self.size
    
    def find(self, element):
        for i in range(self.size):
            if self.list[i]==element:
                return i
        return False
    
    def insert(self, element, after):
        insert_pos = self.find(after)
        if insert_pos:
            self.list.insert(insert_pos+1, element)
            self.size +=1
            return True
        return False
    
    def remove(self, element):
        found_at=self.find(element)
        if found_at:
            del self.list[found_at]
            self.size -=1
            return True
        return False
    
    def clear(self):
        self.list.clear()
        self.size = 0
        self.pos = 0
        
    def __str__(self):
        return f"[{', '.join(list(map(str, self.list)))}]"


    