# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_middle_node(head: ListNode):
    temp_head = head
    slow_node = head
    fast_node = head.next

    while fast_node and fast_node.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    return slow_node

def reverse_linked_list(head):
    slow = None
    curr= head
    fast = head
    while fast:
        fast = curr.next
        curr.next=slow
        slow=curr
        curr=fast
    return slow

def compare_linked_lists(first_head:ListNode , secocd_head:ListNode):
    while first_head and secocd_head:
        if not first_head.val==secocd_head.val:
            return False
        first_head=first_head.next
        secocd_head=secocd_head.next
    return True
def isPalindrome( head: Optional[ListNode]) -> bool:

    if not head.next:
        return True
    mid_node = get_middle_node(head)
    first_half_head = head
    second_half_head = mid_node.next
    mid_node.next = None
    reversed_second_head= reverse_linked_list(second_half_head)
    return compare_linked_lists(first_head=first_half_head , secocd_head=reversed_second_head)


'''adding list of elemnts to linked list'''
head=None
for i in [1]:
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

# ll=isPalindrome(head)
# while ll:
#     print(ll.val,end='\t')
#     ll=ll.next
print(isPalindrome(head))