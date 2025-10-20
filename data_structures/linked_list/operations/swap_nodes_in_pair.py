# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    curr_node= head
    if not head :
        return head
    fast_node = curr_node.next
    head =  fast_node if fast_node else head
    slow_node = None
    while fast_node:
        #swapping nodes
        curr_node.next = fast_node.next
        fast_node.next = curr_node
        #taking slownode for connection
        if slow_node:
            slow_node.next = fast_node
        slow_node = curr_node
        #moving node pointer to next nodes
        fast_node = curr_node.next if curr_node.next else None
        curr_node = fast_node
        fast_node = curr_node.next if curr_node else None

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

ll=swapPairs(head)
while ll:
    print(ll.val,end='\t')
    ll=ll.next