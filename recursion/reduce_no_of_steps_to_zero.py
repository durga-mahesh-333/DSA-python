def numberOfSteps( num: int) -> int:
    def helper(num , step_count):
        if num==0 :
            return step_count
        if num %2 ==1 :
            num-=1
        else:
            num//=2
        return helper(num , step_count+1)
    return helper(num , 0)
        