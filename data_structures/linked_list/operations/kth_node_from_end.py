from data_structures.linked_list.linked_list import LinkedList

# first take the helper node(h.n) move till K position ,
# next stem move curr_node(c.n) and helper node together, to get curr_node to kth position from the end
#Eg: lisked list of 1, 2, 3, 4, 5, 6 |    let k = 5  kth(5th) node from end is 2
#help position moved to 5th (tkh) node till node value 5
# c.n             h.n
#   1  2   3   4   5   6
#
#now move h.n and c.n together till h.n is end of LL
#
#     c.n                   h.n
#   1  2   3   4   5   6
#c.n is final answer kth position from end

def find_kth_node_from_end(ll:LinkedList, k:int):
    curr_node=helper_node=ll.head

    for _ in range(k):
        helper_node=helper_node.next

    while helper_node:
        curr_node=curr_node.next
        helper_node=helper_node.next
    return curr_node.value
