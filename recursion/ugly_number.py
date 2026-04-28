def isUgly(n: int) -> bool:
    if n in [1,2,3,5]: return True
    if n ==0 : return False
    def helper( num: int ):
        if num in [0,1,2,3,5]: return True
        is_factored=False
        if num%2==0:
            num//=2
            is_factored=True
        if num%3==0:
            num//=3
            is_factored=True
        if num%5==0:
            num//=5
            is_factored=True

        if is_factored:
            return helper( num)
        else:
            return False
    return helper( n)
print(isUgly(6))