def check_every_num_positive(list_data):
    def helper(list_val , left , right):
        if left==right:
            return True if list_val[left]>0 else False
        mid = (left+right)//2
        left_val = helper(list_val , left , mid)
        right_val= helper(list_val , mid+1 , right)

        return left_val and right_val
    return helper(list_data, 0 , len(list_data)-1)
print(check_every_num_positive([1,2,3,4,-5,6,7,-8]))
    