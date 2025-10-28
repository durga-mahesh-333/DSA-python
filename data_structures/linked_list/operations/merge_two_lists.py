# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists( list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head1 = list1
    head2 = list2
    if not head1 and head2:
        return head2
    elif not head2 and head1:
        return head1
    elif not head1 and not head2:
        return
    else:
        while list2 :
            if list1.val<= list2.val and ( list1.next and list2.val<=list1.next.val):
                list1_tmp=list1
                list2_tmp=list2

                list1=list1.next
                list2=list2.next

                list1_tmp.next=list2_tmp
                list2_tmp.next=list1

                list1 = list2_tmp
            elif list1.val<= list2.val and ( not list1.next ):
                list1.next = list2
                break
            elif list2.val<=list1.val:
                list1_tmp = list1
                list2_tmp = list2

                list1 = list1.next
                list2 = list2.next

                list2_tmp.next=list1_tmp
                list1=list2_tmp
                head1=list1
            else:
                list1=list1.next

    return head1

'''adding list of elemnts to linked list'''
list1=None
for i in [2]:
    if not list1:
        list1=ListNode(i)
        tail=list1
    else:
        tail.next = ListNode(i)
        tail=tail.next
list2=None
for i in [3]:
    if not list2:
        list2=ListNode(i)
        tail=list2
    else:
        tail.next = ListNode(i)
        tail=tail.next
# printing listNode elements
temp_head=list1
print('ListNode1 created:')
while temp_head:
    print(temp_head.val,end='\t')
    temp_head=temp_head.next
print()
# printing listNode elements
temp_head=list2
print('ListNode2 created:')
while temp_head:
    print(temp_head.val,end='\t')
    temp_head=temp_head.next
print()
print('Printing after operations : ')

ll=mergeTwoLists(list1,list2)
while ll:
    print(ll.val,end='\t')
    ll=ll.next
