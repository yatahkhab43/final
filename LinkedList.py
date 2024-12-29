class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
        
    def delete(self,key):
        current=self.head
        if current and current.data==key:
            self.head=current.next
            current=None
            return
        prev=None
        while current and current.data !=key:
            prev=current
            current=current.next
        if current is None:
            print(key,"Not found")
            return
        prev.next=current.next
        current=None
        
    def travers(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print(None)
        
        
    def revers(self):
        head=self.head
        prev=None
        while head:
           nextN=head.next
           head.next=prev
           prev=head
           head=nextN
        self.head=prev
        
    def middle(self):
        slow,fast=self.head,self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print("Middle ",slow.data)
        
           
            
        
l=LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.travers()
l.middle()
print("Delete")
l.delete(2)
l.travers()
print("Revers a list")
l.revers()
l.travers()
l.middle()