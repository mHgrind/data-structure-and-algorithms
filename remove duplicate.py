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
    
    def remove_duplicates(self):
        current = self.head

    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next