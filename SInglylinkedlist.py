class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class llist:
    def __init__(self):
        self.head= None
    def print_ll(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->", end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head=new_node
    def add_end(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        if self.head==None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.ref
            if n is None:
                print("Node is not present")
            else:
                new_node=Node(data)
                new_node.ref=n.ref
                n.ref=new_node
    def del_begin(self):
        if self.head is None:
            print("Linked list is already empty")
        else:
            self.head=self.head.ref
    def del_end(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def del_by_value(self,x):
        if self.head==None:
            print("Linked list is empty")
            return
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node not present")
        else:
            n.ref=n.ref.ref
    def search(self,x):
        n=self.head
        pos=0
        while n:
            if n.data==x:
                return pos
            n=n.ref
            pos+=1
        return -1
ll1=llist()
n1=Node(20)
ll1.head=n1
n2=Node(57)
n1.ref=n2
ll1.print_ll()
print("After adding element in beginning")
ll1.add_begin(98)
ll1.print_ll()
print("After adding element at the end")
ll1.add_end(69)
ll1.print_ll()
print("After adding after a node")
ll1.add_after(2456,98)
ll1.print_ll()
print("After deleting the last node")
ll1.del_end()
ll1.print_ll()
ll1.search(20)
ll1.add_after(69,88)
ll1.print_ll()
ll1.del_end()
ll1.print_ll()

