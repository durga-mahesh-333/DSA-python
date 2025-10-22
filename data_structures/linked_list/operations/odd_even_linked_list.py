# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    odd_start_node = even_start_node = even_temp_node = odd_temp_node = None
    running_node = head
    index=1
    while running_node:
        curr_node = running_node
        running_node=running_node.next
        curr_node.next = None
        if index%2 ==1 :
            if odd_start_node:
                odd_temp_node.next = curr_node
                odd_temp_node = odd_temp_node.next
            else:
                odd_start_node= curr_node
                odd_temp_node= curr_node
        else:
            if even_start_node:
                even_temp_node.next = curr_node
                even_temp_node = even_temp_node.next
            else:
                even_start_node= curr_node
                even_temp_node= curr_node
        if not running_node:
            odd_temp_node.next = even_start_node
            even_temp_node = None
        index+=1
    return odd_start_node
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

ll=oddEvenList(head)
while ll:
    print(ll.val,end='\t')
    ll=ll.next