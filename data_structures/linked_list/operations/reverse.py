from data_structures.linked_list.linked_list import LinkedList

def reverse_linked_list(linked_list : LinkedList):
    linked_list.head  , linked_list.tail  , curr_node = linked_list.tail , linked_list.head , linked_list.head

    before_node=None
    temp_node=curr_node

    while(curr_node):
        temp_node=curr_node.next
        curr_node.next=before_node
        before_node=curr_node
        curr_node=temp_node

    return linked_list