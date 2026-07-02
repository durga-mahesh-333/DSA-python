def find_max_num(list_data:list):
    def helper(list_val, left , right):
        if left==right:
            return list_val[left]
        mid = (left+right)//2
        left_val=helper(list_val , left , mid)
        right_val= helper(list_val , mid+1, right)

        return left_val if left_val>right_val else right_val
    return helper(list_data,0,len(list_data)-1)

print(find_max_num([4,1,77,8,9]))