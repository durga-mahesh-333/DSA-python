# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_part_list(slow  , curr   , fast  , post_end_node ):
    while not fast== post_end_node:
        fast = curr.next
        curr.next = slow
        slow=curr
        curr = fast


def reverseKGroup(head , k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """
    if k ==1 or k ==0:
        return head
    counter = 1
    k_group_start_node = running_node = head
    k_group_pre_start_node = k_group_end_node = k_group_post_end_node = None
    while running_node :
        if counter == k :
            pass
            k_group_end_node = running_node
            k_group_post_end_node = running_node.next
            reverse_part_list(
                slow= k_group_pre_start_node,
                curr= k_group_start_node,
                fast = k_group_start_node,
                post_end_node=k_group_post_end_node
            )

            if k_group_pre_start_node :
                k_group_pre_start_node.next = k_group_end_node
            else:
                head = k_group_end_node
            k_group_start_node.next = k_group_post_end_node
            k_group_pre_start_node = running_node = k_group_start_node
            k_group_start_node = k_group_post_end_node
            counter=0
        counter+=1
        running_node=running_node.next
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
print('Printing after swap elements : ')

ll=reverseKGroup(head , 5)
while ll:
    print(ll.val,end='\t')
    ll=ll.next
