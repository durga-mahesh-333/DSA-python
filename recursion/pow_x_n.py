import sys
sys.set_int_max_str_digits(1000000000)
def myPow( x: float, n: int) -> float:
    def helper(updt_pow:int , extra_pow:int , powered_val:float ):
        if updt_pow==1:
            return powered_val*powered_val if extra_pow==0 else  powered_val*powered_val*powered_val
        if updt_pow%2==1:
            updt_pow-=1
            extra_pow=1
        updt_powered_val= helper(updt_pow=updt_pow//2,extra_pow=extra_pow , powered_val=powered_val)
        return helper(updt_pow=updt_pow//2,extra_pow=extra_pow , powered_val=updt_powered_val)
    
    return helper(n,0,x)
        
print(myPow(2,11))