#inked list - to make a node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#insert a node at the starting of LL
def insert_at_start(head , new_data):
    new_data = Node(new_data)
    new_data.next = head
    head = new_data
    return head
        
#print fun for linkedlist
def printLL(head):
    temp = head
    while temp:
        print(temp.data , end = "->")
        temp = temp.next
    print("None")
    
node1 = Node(5)
node2 = Node(3)
node3 = Node(24)

node1.next = node2
node2.next = node3
head = node1

head = insert_at_start(head, 11)

printLL(head)
