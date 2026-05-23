
'''My final solution without using lists'''
def lastRemaining( n: int) -> int:
    if n==1: return 1
    n= n-1 if n%2==1 else n
    def helper(val,reduced_val,loop_count):
        if reduced_val==1:
            return val
        if (loop_count-1)%2==1 or reduced_val%2==1:
            if loop_count==1:
                val-=2
            else:
                val-=2**(loop_count-1)
        # print(f'for loop count:{loop_count}, reduced_value:{reduced_val} , val:{val}')
        return helper(val,reduced_val//2,loop_count+1)
    return helper(n,n,1)
print(lastRemaining(2))


'''
famous optimal solution on leetcode
def lastRemaining( n: int) -> int:
    head = 1
    step = 1
    res = n
    left = True 
    while res >= 2:
        if left or res % 2 == 1:
            head += step
        step *= 2
        left = not left
        res //= 2
    
    return head
'''


''' another brute force
def lastRemaining_brute( n: int) -> int:
    if n==1: return 1
    # print(f'differen value will be : {2**(recur_count-1)}')
    intial_list_after_first_removal=[i for i in range(2,n+1,2)]
    
    # print(f'list start and end at loop {1} : {[intial_list_after_first_removal[0], intial_list_after_first_removal[-1]]}== {len(intial_list_after_first_removal)}')
    def helper(list_data, count):
        new_list=[]
        if len(list_data)==1:
            # print(f'Closed at loop {count} , then power value (loop-1) : {2**(count-1)}')
            return list_data[0]

        for i in range(len(list_data)-2,-1,-2):
            new_list.append(list_data[i])
        print(f'for loop count:{count}, reduced_value:{len(list_data)} , val:{list_data[0],list_data[-1]}')
        return helper(new_list,count+1)
    return helper(intial_list_after_first_removal,2)'''


'''#Brute solution 
def lastRemaining( n: int) -> int:
    if n==1: return 1
    intial_list=[i for i in range(1,n+1)]

    def removal_recursion(data_list):
        new_list=[]
        if len( data_list )==1:
            return data_list[0]
        for i in range(1,len(data_list)+1):
            if i%2==0:
                new_list.append(data_list[i-1])
        return removal_recursion(new_list[::-1])
    return removal_recursion(intial_list)'''
        