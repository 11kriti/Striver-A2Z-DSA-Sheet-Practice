#inked list - to make a node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#find the length of LL
def lengthOfLL(head):
    if head is None:
        return None
    count = 0
    temp = head
    while temp is not None:
        temp = temp.next
        count +=1
    return count
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

#head = insert_at_start(head, 11)
#head = insert_node_at_end(head , 25)
#head = delete_from_start(head)
length = lengthOfLL(head)
print("Length of Linked List:", length)
printLL(head)
