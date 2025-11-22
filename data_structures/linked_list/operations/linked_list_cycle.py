# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    if not( head and head.next  and head.next.next):
        return False
    curr_node = head
    fast_node= head.next.next
    while fast_node and fast_node.next:
        if curr_node!=fast_node:
            curr_node=curr_node.next
            fast_node=fast_node.next.next
        else:
            return True
    return False


def creating_inpit_list(list_data , position):
    ll=None
    for i in list_data:
        if not ll:
            ll=ListNode(i)
            tail=ll
        else:
            tail.next=ListNode(i)
            tail=tail.next
    if position==-1:
        return ll
    else:
        positon_node = ll
        pos=1
        while pos<=position:
            positon_node=positon_node.next
            pos+=1
        tail.next=positon_node
        return positon_node



input_ll=creating_inpit_list([3,2,0,-4],1)

# while input_ll:
#     print(input_ll.val , end='\t')
#     input_ll=input_ll.next
print(hasCycle(input_ll))