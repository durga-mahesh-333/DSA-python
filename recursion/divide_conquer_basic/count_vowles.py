def count_vowels(str_val):
    def helper(str_ip , left , right):
        if left == right : 
            return 1 if str_ip[left].lower() in ['a','e','i','o','u'] else 0
        
        mid = (left+right) //2
        left_val = helper(str_ip , left , mid )
        right_val= helper(str_ip , mid+1 , right)

        return left_val+right_val
    return helper(str_val , 0 , len(str_val)-1)
print(count_vowels('MaheshA'))