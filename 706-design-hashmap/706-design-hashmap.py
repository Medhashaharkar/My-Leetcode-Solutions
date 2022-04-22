class Node:
    def __init__(self,value):
        self.next = None
        self.val = value
        
class MyHashMap:

    def __init__(self):
        self.heads = []

    def put(self, key: int, value: int) -> None:
        
        node = Node(value)
        
        keynode = None
        
        for h in self.heads:
            if (h.val == key):
                keynode = h
                break
        
        if (keynode == None):
            keynode = Node(key)
            self.heads.append(keynode)
            print("Appended",keynode.val,"to heads")
            keynode.next = node
            print("Appended",node.val,"to keynode",keynode.val)
        else:
            keynode.next = node
            print("Updated",node.val,"of keynode",keynode.val)
    
#        else:
#           ptr = keynode
#           while ptr.next != None:
#                ptr = ptr.next
#            ptr.next = node
                        

    def get(self, key: int) -> int:
        
        for h in self.heads:
            if (h.val == key):
                ptr = h
                while ptr.next != None:
                    ptr = ptr.next
                return ptr.val
        return -1
        

    def remove(self, key: int) -> None:
        for h in self.heads:
            if (h.val == key):
                self.heads.remove(h)
                break
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)