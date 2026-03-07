def isPowerOfTwo( n: int) -> bool:
    if n==0:
        return False
    if n in [1,2]:
        return True

    def helper(pow):
        req_val= 2**pow
        if req_val > n:
            return False
        if req_val==n:
            return True
        return helper(pow+1)
    return helper(2)
print(isPowerOfTwo(0))
    

