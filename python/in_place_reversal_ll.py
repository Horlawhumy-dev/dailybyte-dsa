


def in_place_reversal_ll(head):

    current, previous = head, None

    next = None

    while current != None:

        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous
