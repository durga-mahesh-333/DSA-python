# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween( head, left, right):
    """
    :type head: Optional[ListNode]
    :type left: int
    :type right: int
    :rtype: Optional[ListNode]
    """
    if left==right:
        return head
    pre_slice_head = slice_head = slice_tail  = post_slice_tail = slow_head =None
    temp_head = head
    index = 1
    # getting positiong of left and right nodes with slice_head and slice_tail
    while temp_head:
        if index== left :
            pre_slice_head= slow_head
            slice_head = temp_head
        elif index == right:
            slice_tail = temp_head
            post_slice_tail =temp_head.next
        index+=1
        slow_head = temp_head
        temp_head=temp_head.next


    slow=slice_head
    fast=curr=slice_head.next
    # reversing the the slice or node between the inputs (left and right)
    while(not curr==post_slice_tail):
        fast=curr.next
        curr.next = slow
        slow=curr
        curr=fast

    #assiging the reversed part to perfect position  with remaining nodes
    if pre_slice_head:
        pre_slice_head.next = slice_tail
    else:
        head = slice_tail
    slice_head.next = post_slice_tail
    return head


'''adding list of elemnts to linked list'''
head=None
for i in [1,2,3,4,5,6]:
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
print('Printing after reverse between elements : ')
slice=reverseBetween(head , 1, 4  )
while slice:
    print(slice.val,end='\t')
    slice=slice.next


