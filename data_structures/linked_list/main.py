from data_structures.linked_list import LinkedList
from data_structures.linked_list.operations.binary_to_decimal import calculate_binary_to_decimal
from data_structures.linked_list.operations.partition_list import partition_list_by_value

ll = LinkedList(1)
ll.append(4)
ll.append(3)
ll.append(2)
ll.append(1)

ll.print_list()

x= 3
print(f'after partition by {x}: ')
partition_list_by_value(ll,3).print_list()

