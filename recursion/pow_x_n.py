import sys
sys.set_int_max_str_digits(1000000000)
def myPow( x: float, n: int) -> float:
        if x==0: return 0
        if abs(x)==1: 
             return abs(x) if n%2==0 else x
        updt_pow=abs(n)
        def helper(given_val:float , pow_val: float , exp:int, extra_exp:int , helper_exp:int , recur:int):
            print(f'pow_val={pow_val} , exp={exp} , exta_exp={extra_exp} ')
            if exp==1 and extra_exp==0: return pow_val,extra_exp
            if exp==1 and extra_exp==1: return pow_val*given_val,extra_exp-1
            if exp%2==1:
                print(f'\t helper exp : {helper_exp}')
                extra_exp+=helper_exp
                exp-=1
            print(f'\t updtd exp:{exp} , updtd ext_exp:{extra_exp}')
            exp//=2
            pow_val*=pow_val
            
            print(f'\t before final cond exp:{exp}')
            if exp>1:
                return helper(given_val=given_val , pow_val=pow_val , exp=exp,extra_exp=extra_exp , helper_exp=helper_exp*2, recur=recur+1)
            elif exp==1 and extra_exp==1: 
                 return helper(given_val=given_val , pow_val=pow_val , exp=exp,extra_exp=extra_exp , helper_exp=1,recur=0)
            else:
                 return helper(given_val=given_val , pow_val=pow_val , exp=extra_exp,extra_exp=0 , helper_exp=1,recur=0)
        pow_val,ext_pow = helper(x,x,updt_pow,0,1,0)
        
        return  pow_val,ext_pow
        def helper_ext_pow(given_val,pow_val,ext_pow):
            if ext_pow==0:
                return pow_val
            return helper_ext_pow(given_val , pow_val*given_val , ext_pow-1) 
           
        # req_value= helper_ext_pow(x,pow_val,ext_pow)
        # if n <0 : 
        #      return 1/req_value
        # else:
        #      return req_value
print(myPow(2,7))