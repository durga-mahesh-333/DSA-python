def integerReplacement( n: int) -> int:
    def helper_bin(num,loop_count):
        if num==1 or num==0:
            return loop_count   
        if num==2:
            return loop_count+1
        if num==3:
            return loop_count+2 
        if num%2==0:
            num//=2
        else:
            if ((num-1)//2)%2==0:
                num-=1
            elif ((num+1)//2)%2==0:
                num+=1
        return helper_bin(num,loop_count+1)
    
    return helper_bin(n,0) 

print(integerReplacement(7 ))





