# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    temp_head= head
    length = 1
    rotation = 0
    tail = before_tail = None
    while head.next:
        head=head.next
        tail=head
        length+=1
    head=temp_head
    tail.next = temp_head

    if k>length:
        k=k%length
    elif length==k :
        tail.next=None
        return temp_head
    if k :
        k=length-k
        while rotation<k :
            helper_head=head
            head=head.next
            tail=helper_head
            rotation+=1

    tail.next=None
    return head


'''adding list of elemnts to linked list'''
head=None
for i in [1,2,3,4,5]:
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

ll=rotateRight(head,k=2)
while ll:
    print(ll.val,end='\t')
    ll=ll.next


