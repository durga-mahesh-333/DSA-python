
def addDigits( num: int) -> int:
    if num < 10 : 
        return num
    def helper(num:int , sum_val: int):
        if num==0 and sum_val<10:
            return sum_val
        if num==0 and sum_val>=10:
            return helper(sum_val , 0)
        sum_val+=num%10
        num=num//10
        return helper(num , sum_val)
    return helper(num , 0 )


print(f'sum is {addDigits(4936)}')