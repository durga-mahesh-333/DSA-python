
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        node = Node(value)
        self.head= node
        self.tail= node
        self.length=1

    def print_list(self):
        current_node=self.head
        print("Linked List values: ")
        for _ in range(self.length):
            print(current_node.value , end='\t')
            current_node=current_node.next
        print()

    def append(self,value):
        node=Node(value)
        print(f"Appending value: {value} at end of the list")
        if not self.length:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.tail.next=node
            self.tail=node
            self.length += 1
        return True

    def prepend(self , value):
        node = Node(value)
        print(f"Prepending value: {value} at start of the list")
        if not self.length:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.next=self.head
            self.head=node
            self.length += 1
        return True

    def pop_first(self):
        popped_value = None
        if not self.length:
            print('No elements available in Linked list to pop')
        elif self.length == 1:
            popped_value = self.head.value
            self.head = self.tail = None
            print(f"Popped value: {popped_value} from first of the list")
            self.length -= 1
        else:
            popped_value = self.head.value
            next_node = self.head.next
            self.head.next = None
            self.head=next_node
            print(f"Popped value: {popped_value} from first of the list")
            self.length -= 1
        return popped_value

    def pop(self):
        popped_value = None
        if not self.length:
            print('No elements available in Linked list to pop')

        elif self.length == 1:
            popped_value = self.tail.value
            self.head = self.head = None
            print(f"Popped value: {popped_value} from last of the list")
            self.length -= 1
        else:
            current_node=self.head
            for _ in range(self.length):
                if current_node.next==self.tail:
                    popped_value=self.tail.value
                    current_node.next=None
                    self.tail=current_node
                    break
                current_node=current_node.next

            self.length -= 1

            print(f"Popped value: {popped_value} from last of the list")

        return popped_value
    def get(self, index):
        if not self.length > index >= 0  :
            print(f"Index provided is {index}. Index must between 0 and {self.length-1} for this linked list")
            return None
        curr_node = self.head
        for i in range(self.length):
            if i == index:
                print(f"value at index {index} is {curr_node.value}")
                return curr_node.value
            curr_node=curr_node.next
    def set(self, index , value):
        if not self.length > index >= 0  :
            print(f"Index provided is {index}. Index must between 0 and {self.length-1} for this linked list")
            return None
        curr_node = self.head
        for i in range(self.length):
            if i == index:
                print(f"value set for index:{index} from  {curr_node.value} to {value}")
                curr_node.value=value
                return True
            curr_node=curr_node.next
    def insert(self,value , index):

        if not self.length >= index >= 0  :
            print(f"Insertion of value {value} failed.Index provided is {index}. Index must between 0 and {self.length} for this linked list")
            return None
        if not self.length or index==0:
            self.prepend(value)
            print(f"Insertion completed.Value:{value} added at index:{index}")
            return True
        if index==self.length:
            self.append(value)
            print(f"Insertion completed.Value:{value} added at index:{index}")
            return True
        node = Node(value)
        curr_node=prev_node=self.head
        curr_index=0
        for _ in range(self.length):
            if curr_index==index:
                prev_node.next=node
                node.next=curr_node
                print(f"Insertion completed.Value:{value} added at index:{index}")
                self.length+=1
                return True
            curr_index+=1
            prev_node=curr_node
            curr_node=curr_node.next

    def remove(self, index):
        if not self.length:
            print(f"Remove failed.No elements available i n linked list")
            return None
        if not self.length >= index >= 0:
            print(f"Remove failed.Index provided is {index}. Index must between 0 and {self.length} for this linked list")
            return None
        if  index == 0:
            print(f"Remove completed.Value:{self.pop_first()} removed from index:{index}")
            return True
        if index == self.length-1:
            print(f"Remove completed.Value:{self.pop()} removed from index:{index}")
            return True
        curr_node = prev_node = self.head
        curr_index = 0
        for _ in range(self.length):
            if curr_index == index:
                prev_node.next=curr_node.next
                self.length -= 1
                print(f"Remove completed.Value:{curr_node.value} removed from index:{index}")
                return True
            curr_index += 1
            prev_node = curr_node
            curr_node = curr_node.next

ll = LinkedList(5)
ll.append(6)
ll.print_list()
print(f'Length of the linked List: {ll.length}')
ll.prepend(0)
ll.print_list()
print(f'Length of the linked List: {ll.length}')
ll.get(1)
ll.get(0)
ll.get(6)
ll.get(2)
ll.set(0,100)
ll.print_list()
ll.pop_first()
ll.print_list()

ll.insert(1000 ,1)
ll.print_list()
print(f"Length of the list :{ll.length}")


ll.remove(1)
ll.print_list()


ll.remove(1)
ll.print_list()
print(f"Length of the list :{ll.length}")

ll.remove(0)
ll.print_list()
print(f"Length of the list :{ll.length}")