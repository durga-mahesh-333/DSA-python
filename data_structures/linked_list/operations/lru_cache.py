class ListNode(object):
    def __init__(self, key ,val, next=None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head : ListNode = None
        self.tail :ListNode = None
        self.storage = 0
    def get(self, key: int) -> int:
        if not self.storage:
            return
        if self.head.key== key :
            return self.head.val
        if self.tail.key== key :
            return self.tail.val

        curr = self.head.next
        prev = None
        while curr and curr!=self.tail:
            if curr.key==key:
                prev.next = curr.next
                curr.next = self.tail.next
                self.tail.next = curr
                self.tail = curr
                return curr.val
            prev=curr
            curr=curr.next
        return -1

    def put(self, key: int, value: int) -> None:
        temp_head = self.head
        while temp_head:
            if temp_head.key == key :
                temp_head.val=value

                if self.storage ==1 or temp_head==self.tail:
                    return
                elif temp_head==self.head:
                    prev_head.next=temp_head.next
                else:
                    self.head=temp_head.next #if temp_head.next else temp_head

                temp_head.next = self.tail.next
                self.tail.next = temp_head
                self.tail = temp_head

                return
            prev_head= temp_head
            temp_head=temp_head.next
        if (not self.storage) or self.capacity==1:
            self.head=ListNode(key, value)
            self.tail=self.head
            self.storage=1
            return None
        elif self.storage<self.capacity:
            self.storage+=1
        else:
            temp = self.head
            next = temp.next
            temp.next = None
            self.head=next

        self.tail.next = ListNode(key, value)
        self.tail = self.tail.next





operations=["LRUCache","get","put","get","put","put","get","get"]
data = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
#      [null,-1,null,-1,null,null,2,6]

# [2, 1] ,
output=[]
cache: LRUCache = None

#expected = [null,null,1,null,-1.
#-]

for index in range(0,len(operations)):
    if operations[index] == "LRUCache":
        cache=LRUCache(data[index][0])
        output.append(None)
    elif operations[index] == "put":
        cache.put(key=data[index][0],value=data[index][1])
        output.append(None)
    elif operations[index] == "get":
        output.append(cache.get(key=data[index][0]))

head= cache.head

while head:
    print(f"{head.key}:{head.val}" , end=',\t')
    head=head.next
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

print(output)