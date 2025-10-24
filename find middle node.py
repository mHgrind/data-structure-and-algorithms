class Node: # creation du noeud
    def __init__(self,value): # construction du noeud en lui ajoutant sa valeur 
        self.value = value # la valeur du noeud
        self.next = None # le pointeur du noeud

        
class LinkedList:
    def __init__(self,value): # creation de la liste de noeud
        new_node = Node(value) 
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self, value):
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
   
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""