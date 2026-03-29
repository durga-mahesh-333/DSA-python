import sys
sys.set_int_max_str_digits(1000000000)
def myPow( x: float, n: int) -> float:
    if n==0: return 1
    if n==1: return x
    if abs(x)==1 and n<0 :
        return abs(x) if n%2==0 else x
    def helper(req_val:float, expo:int):
        if expo==0:
            return 1
        updt_val=helper(req_val, expo//2)
        return updt_val*updt_val if expo%2==0 else updt_val*updt_val*req_val
    
    final_val= helper(x,abs(n))
    return final_val if n>0 else 1/final_val

        
print(myPow(-1,-2147483648))