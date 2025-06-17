#inked list - to make a node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        
#print fun for linkedlist
def printLL(head):
    temp = head
    while temp:
        print(temp.data , end = "->")
        temp = temp.next
    print("None")
    
node1 = Node(5)
node2 = Node(3)
node3 = node(24)

node1.next = node2
node2.next = node3

printLL(node1)
