class LinkedListNode:
    def __init__(self,value):
        self.value=value
        self.next=None

def partition_list_by_value(head:LinkedListNode , x) -> LinkedListNode:
    smaller_head=larger_head=larger_tail=small_tail=None
    curr_node = head
    while(curr_node):
        present_value=curr_node.value
        temp = curr_node
        curr_node = curr_node.next
        temp.next = None
        if present_value>=x:
            if not larger_head:
                larger_head=temp
                larger_tail=larger_head
            else:
                larger_tail.next=temp
                larger_tail=temp
        else:
            if not smaller_head:
                smaller_head = temp
                small_tail = smaller_head
            else:
                small_tail.next = temp
                small_tail = temp
    if not smaller_head and not larger_head:
        return
    if not smaller_head and larger_head:
        return larger_head
    elif smaller_head and not larger_head:
        return smaller_head
    else:
        small_tail.next=larger_head
        return smaller_head


input_list=[1,4,2,3,5,2]
x= 3
print(f"Input : {input_list} , x= {x}")
#############################################
# adding data to linked list using for loop #
#############################################
head=tail=None
for i in input_list:
    ln=LinkedListNode(i)
    if not head:
        head = ln
        tail = head
    else:
        tail.next=ln
        tail=ln

req_output_ll = partition_list_by_value(head, x)
print("Linked list after parition by value:")
ouput_for_print=[]
while req_output_ll :
    ouput_for_print.append(req_output_ll.value)
    req_output_ll=req_output_ll.next
print(f"Output : {ouput_for_print}")


