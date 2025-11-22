# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not( head and head.next  and head.next.next):
        return
    curr_node = head
    fast_node= head.next.next
    has_loop=False
    while fast_node and fast_node.next:
        if curr_node!=fast_node:
            curr_node=curr_node.next
            fast_node=fast_node.next.next
        else:
            has_loop=True
            break
    if has_loop:
        #find cycle length
        l_node=fast_node.next
        loop_length=1
        while not l_node==fast_node:
            l_node=l_node.next
            loop_length+=1

        curr_node=fast_node=head
        #move one pointer forward to loop length from start
        while loop_length:
            fast_node=fast_node.next
            loop_length-=1
        #finding loop start
        while not fast_node==curr_node:
            curr_node=curr_node.next
            fast_node=fast_node.next
        return curr_node

    else:
        return


def creating_input_list(list_data, position):
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
        return ll



input_ll=creating_input_list([1, 2], 0)
cycle_pos= detectCycle(input_ll)
print(f'cycle_pos.val:{cycle_pos.val}')
