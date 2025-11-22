# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode( headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    a, b = headA, headB

    # Traverse both lists; when a pointer hits the end, redirect it to the other list's head.
    # If there is an intersection, a and b will meet at the node; otherwise both will be None.
    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a



list1=[4,1,8,4,5]
list2=[5,6,1,8,4,5]
skipA = 2
skipB = 3
intersect_val = 8
def generate_input_linked_lists_for_test(list1 , list2 , skipA,skipB,intersect_val ):
    linked_listA = None
    intersect_nodeA=None
    index=0
    for i in list1:
        if not linked_listA:
            linked_listA = ListNode(i)
            tail = linked_listA
        else:
            tail.next = ListNode(i)
            tail = tail.next
        if skipA==index:
            intersect_nodeA=tail
        index+=1
    linked_listB = None
    if not intersect_val==0:
        list2=list2[:3]
        tail_B=None
        for i in list2:
            if not linked_listB:
                linked_listB = ListNode(i)
                tail_B = linked_listB
            else:
                tail_B.next = ListNode(i)
                tail_B = tail_B.next
        tail_B.next=intersect_nodeA
        return linked_listA , linked_listB
    else:
        for i in list2:
            if not linked_listB:
                linked_listB = ListNode(i)
                tail_B = linked_listB
            else:
                tail_B.next = ListNode(i)
                tail_B = tail_B.next
        return linked_listA ,linked_listB

print()
print('Printing after reverse between elements : ')
head1,head2=generate_input_linked_lists_for_test(list1 , list2 , skipA,skipB,intersect_val )
ll=getIntersectionNode( head1, head2)

while ll :
    print(ll.val , end='\t')
    ll=ll.next