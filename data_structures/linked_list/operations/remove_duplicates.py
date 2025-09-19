from data_structures.linked_list.linked_list import LinkedList

def remove_duplicates_from_linked_list(ll:LinkedList):
    curr_node=ll.head
    # dup_check_node = curr_node.next
    while curr_node:
        dup_check_node = curr_node.next
        while dup_check_node:
            if curr_node.value==dup_check_node.value: #1=1
                curr_node.next = dup_check_node.next
                dup_check_node = curr_node.next
            else:
                dup_check_node = dup_check_node.next
        curr_node = curr_node.next
    return ll