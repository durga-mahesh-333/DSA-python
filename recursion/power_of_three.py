def isPowerOfThree( n: int) -> bool:
    if n==0: return False
    def helper(num):
        if num ==1:
            return True
        if num%3==0:
            num//=3
            return helper(num)
        else:
            return False
    return helper(n)
print(isPowerOfThree(27))