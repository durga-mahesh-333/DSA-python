from data_structures.linked_list.linked_list import LinkedList

def get_middle_node(ll : LinkedList):
    slow_node=ll.head
    fast_node=ll.head.next

    while fast_node and fast_node.next:
        slow_node=slow_node.next
        fast_node=fast_node.next.next

    return slow_node