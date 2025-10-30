class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

    def make_empty(self):
        self.head = None
        self.length = 0

    # ✅ Méthode reverse_between
    def reverse_between(self, left, right):
        # Cas trivial : liste vide ou intervalle de taille 1
        if not self.head or left == right:
            return

        # 1️⃣ Dummy node pour simplifier le code
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        # 2️⃣ Avancer jusqu'à l'élément avant la zone à inverser
        for _ in range(left):
            if not prev.next:
                return  # left dépasse la longueur
            prev = prev.next

        # 3️⃣ Initialiser les pointeurs
        start = prev.next
        then = start.next

        # 4️⃣ Inverser la portion [left, right]
        for _ in range(right - left):
            if not then:
                break
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        # 5️⃣ Mettre à jour le head
        self.head = dummy.next


# ---------------- TESTS ----------------

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
EXPECTED OUTPUT:
----------------
Original linked list: 
1 -> 2 -> 3 -> 4 -> 5 -> None
Reversed sublist (2, 4): 
1 -> 2 -> 5 -> 4 -> 3 -> None
Reversed entire linked list: 
3 -> 4 -> 5 -> 2 -> 1 -> None
Reversed sublist of length 1 (3, 3): 
3 -> 4 -> 5 -> 2 -> 1 -> None
Reversed empty linked list: 
Empty -> None
"""
