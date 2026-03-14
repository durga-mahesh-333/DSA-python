def myPow( x: float, n: int) -> float:
       
        def helper(given_val:float , pow_val: float , exp:int, extra_exp:int , helper_exp:int , recur:int):
            if exp==1: return pow_val,extra_exp
            if exp%2==1:
                extra_exp=1
                extra_exp*=helper_exp
                exp-=1
            
            exp//=2
            pow_val*=pow_val
            
            return helper(given_val , pow_val , exp,extra_exp , helper_exp*2, recur+1)

        pow_val,ext_pow = helper(x,x,n,0,1,0)
        return  pow_val,ext_pow
        def helper_ext_pow(given_val,pow_val,ext_pow):
            if ext_pow==0:
                return pow_val
            return helper_ext_pow(given_val , pow_val*given_val , ext_pow-1) 
        return helper_ext_pow(x,pow_val,ext_pow)
print(myPow(2,13))