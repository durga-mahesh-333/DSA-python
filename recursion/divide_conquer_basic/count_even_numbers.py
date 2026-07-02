def count_even_number(list_data):
    def helper(list_val , left , right):
        if left==right:
            return 0 if list_data[left]%2==1 else 1
        mid=(left+right)//2
        left_val=helper(list_val , left , mid)
        right_val=helper(list_val , mid+1 , right)

        return left_val + right_val
    return helper(list_data,0 , len(list_data)-1)

print( count_even_number([1,2,3,5,6,7,8,9,0]) )


                

