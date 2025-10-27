# Definition for singly-linked list.
from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList( head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    if not head or not( head.next ):
        return

    # finding middle of liknked list : start
    fast = head.next
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid= slow
    # finding middle of liknked list : end

    first_half_head = head
    second_half_head=mid.next
    mid.next=None

    # rev of liknked list : start
    ll=second_half_head
    if not ll.next:
        rev_second_half = ll
    else:
        slow_for_rev = None
        curr_for_rev= ll
        fast_for_rev =curr_for_rev.next
        while(fast_for_rev):
            fast_for_rev = curr_for_rev.next
            curr_for_rev.next=slow_for_rev
            slow_for_rev=curr_for_rev
            curr_for_rev=fast_for_rev
        rev_second_half=slow_for_rev
    # rev of liknked list : end

    while head and rev_second_half:
        slow_fhh=head
        slow_shh=rev_second_half
        head=head.next
        rev_second_half=rev_second_half.next

        slow_fhh.next=slow_shh
        slow_shh.next=head

    return first_half_head


'''adding list of elemnts to linked list'''
head=None
for i in [1,2,3]:
    if not head:
        head=ListNode(i)
        tail=head
    else:
        tail.next = ListNode(i)
        tail=tail.next


# printing listNode elements
temp_head=head
print('ListNode created:')
while temp_head:
    print(temp_head.val,end='\t')
    temp_head=temp_head.next
print()
print('Printing after swap elements : ')

ll=reorderList(head)
while ll:
    print(ll.val,end='\t')
    ll=ll.next

