def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head

    # Étape 1 : avancer fast de k pas
    for _ in range(k):
        if fast is None:   # si la liste est plus courte que k
            return None
        fast = fast.next

    # Étape 2 : avancer les deux jusqu’à la fin
    while fast is not None:
        slow = slow.next
        fast = fast.next

    # Étape 3 : slow est sur le kᵗʰ depuis la fin
    return slow 
