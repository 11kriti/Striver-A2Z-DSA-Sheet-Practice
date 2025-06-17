#create a node for DLL
class Node:
    def __init__(self,data):
        self.data = data
        self .prev = None
        self.next = None
        
#insert node at starting 
def insert_node_at_start(head , new_data):
    new_node = Node(new_data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node
#print a DLL
def printDLL(head):
    temp = head
    while temp:
        print(temp.data , end = "<->")
        temp = temp.next
    print("None")
    
node1 = Node(24)
node2 = Node(11)
node3 = Node(25)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
head = node1

head = insert_node_at_start(head , 1)

printDLL(head)
