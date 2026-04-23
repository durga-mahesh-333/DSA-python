def climbStairs(n: int) -> int:
    if n==1 or n==0 : return n
    storage={}
    def helper(num):
        if num in storage:
            return storage[num]
        if num==0 : return 0
        if num==1 : return 1
        storage[num]= helper(num-1)+helper(num-2)
        return storage[num]
    return helper(n+1)
print(climbStairs(38))