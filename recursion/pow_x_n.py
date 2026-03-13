def myPow( x: float, n: int) -> float:
       
        def helper(given_val:float , pow_val: float , exp:int):
            exp_red=False
            if exp==1: return pow_val
            if exp%2==1:
                exp_red=True
                exp-=1
            
            exp//=2
            pow_val*=pow_val
            pow_val=pow_val*given_val if exp_red else pow_val/given_val
            return helper(given_val , pow_val , exp)

        return helper(x,x,n)
print(myPow(2.0 , 10))