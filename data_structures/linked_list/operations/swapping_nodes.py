# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def swapNodes( head, k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """
    #getting the nodes at given position
    k_node_from_start=head
    pre_k_node_from_start = None
    index=1
    #getting nodes from k node from start , k node from end , previous k node from start , post k node start , previous knode from end
    while not index==k:
        pre_k_node_from_start = k_node_from_start
        k_node_from_start=k_node_from_start.next
        index+=1

    post_k_node_from_start = k_node_from_start.next
    k_node_from_end=head
    pre_k_node_from_end = None
    temp_node=k_node_from_start.next
    while temp_node:
        pre_k_node_from_end=k_node_from_end
        temp_node=temp_node.next
        k_node_from_end = k_node_from_end.next

    # assigning node for snapping
    # if pre k node from start is none i,e k node from start is first element , we cannot get none.next so skip this if it is none
    if pre_k_node_from_start:
        #if not none , we assing k node from ent to the pre k node from start i,e we are starting a link fro swap for k node from start element
        pre_k_node_from_start.next = k_node_from_end
    else :
        # if node before k node from start is none , that means k node from start is the first or head node , so we are assigning head to the node with which it swaps
        # similary vice versa for knode from end
        head = k_node_from_end

    #here we are assiging knode next address to the node after knode from end i,e knode from ent next
    k_node_from_start.next = k_node_from_end.next

    if  post_k_node_from_start==k_node_from_end:
        # if post knode from start i,e knode from start next element is equal to knode from end , that means if thw knode from start and knode from end are side by side
        # we assing k node from end next to knode from start
         k_node_from_end.next = k_node_from_start
    else:
        # if not above scenario , then we assign k node from end next  post k node from start and pre k node from end next addressing to k node from start
        k_node_from_end.next = post_k_node_from_start
        if pre_k_node_from_end:
            pre_k_node_from_end.next  = k_node_from_start
        else:
            head = k_node_from_start
    return head




'''adding list of elemnts to linked list'''
head=None
tail=None
for i in [100,90]:#[7,9,6,6,7,8,3,0,9,5]:
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

ll=swapNodes(head,2)
while ll:
    print(ll.val,end='\t')
    ll=ll.next