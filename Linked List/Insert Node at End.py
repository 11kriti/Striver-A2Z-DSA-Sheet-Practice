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
    
#insert node at the end
def insert_node_at_end(head , new_data):
    new_node = Node(new_data)
    if head is None:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
        
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
head = insert_node_at_end(head , 25)

printLL(head)
