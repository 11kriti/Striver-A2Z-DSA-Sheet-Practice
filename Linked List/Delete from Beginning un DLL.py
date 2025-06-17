class Node:
    def __init__(self,data):
        self.data = data
        self .prev = None
        self.next = None
        
#delete from starting
def delete_from_start(head):
    if head is None:
        return None
    head = head.next
    if head is not None:
        head.prev = None
    return head
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

#head = insert_node_at_start(head , 1)
#head = insert_at_end(head, 111)
delete_from_start(head)

printDLL(head)
