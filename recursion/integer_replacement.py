def integerReplacement( n: int) -> int:
    if n==1 or n==0 : return 0
    def helper_bin(num,num_of_oper,loop_count):
        if num==1:
            return loop_count   
        bin_val=num%2
        num//=2
        if bin_val==1: num+=1
        return helper_bin(num,num_of_oper,loop_count+1)
    
    return helper_bin(n,0,0) + n%2

print(integerReplacement(1))





