from data_structures.linked_list import LinkedList


def calculate_binary_to_decimal(ll:LinkedList):
    curr_node=ll.head
    dec_value=0
    while(curr_node):
        dec_value=2*dec_value+curr_node.value
        curr_node=curr_node.next

    return dec_value