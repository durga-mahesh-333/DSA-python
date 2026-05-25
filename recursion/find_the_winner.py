def findTheWinner( n: int, k: int) -> int:
    if k==1 or n==1 : return n
    list_from_input=[i+1 for i in range(0,n) ]
    def helper(reordered_list):
        if len(reordered_list)==1:
            return reordered_list[0]
        
        updated_counter = k%len(reordered_list) if k> len(reordered_list) else k
        
        if not updated_counter : updated_counter=len(reordered_list)
        updated_reordered_list=reordered_list[updated_counter:]+reordered_list[:updated_counter-1]
        return helper(updated_reordered_list)
    return helper(list_from_input)

print(findTheWinner(7,8))