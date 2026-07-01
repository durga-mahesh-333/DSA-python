def num_of_chars(input_str:str):
    def helper(str_val , left , right ):
        if left==right:
            return 1
        mid = ((left)+(right))//2
        left_count = helper(str_val , left , mid )
        right_count = helper(str_val , mid+1 , right )
        return left_count+right_count
    return helper(input_str,0,len(input_str)-1)

print(num_of_chars('chatgpts'))
