
def kthGrammar( n: int, k: int) -> int:
    def helper(row , postition , expect_val=0 ):
        if row==1:
            return expect_val
        half = 2**(row-1)//2
        if postition>half : 
            postition-=half
            expect_val=1-expect_val
        return helper(row-1 , postition, expect_val)
    return helper(n,k,0)
    # if n==1 and k==1: return 0
    # helper_str=''
    # if n>=2 : helper_str='01'
        
    # def second_part_gen(str_val:str , index:int , req_part:str):
    #     if index==len(str_val):
    #         return req_part
    #     req_part+=str(1-int(str_val[index]))
    #     return second_part_gen(str_val , index+1 , req_part)
    # def helper(row_val:int , final_str:str):
    #     if row_val==n:
    #         return final_str
    #     if (row_val)%2==1: 
    #         sec_part=second_part_gen(final_str , 0 , '')
    #     else : 
    #         sec_part= final_str[::-1]
    #     req_str=final_str+sec_part
    #     # print(f'second_part : {sec_part}  ')
    #     return helper(row_val+1 , req_str)

    # kth_val= helper(2,helper_str)#[k-1]
    # return kth_val

print(kthGrammar(5,16))

# print(bin(30))#.count('1'))
'''
n=2 01
n=3 0110
n=4 01101001
n=5 0110100110010110
n=6 01101001100101101001011001101001
n=7 0110100110010110100101100110100110010110011010010110100110010110
n=8 01101001100101101001011001101001100101100110100101101001100101101001011001101001011010011001011001101001100101101001011001101001

'''

'''
problem explaination 

n=1 and row has '0'
from n=2 , if we see 0 in previous row then add '01' to next row, and if we see '1' in previous row then add '10' to next row 
so let n be row num

n=1         0
n=2       0     1
n=3     0   1  1   0
n=4   0  1 1 0 1 0 0 1   
.
.
.
.

if we see from 3rd row pattern is repeating like oppsite

the first half of the values are (let take 1 0) values of previus row and second half is the opposite of the previos row (0 1) (1 in place of 0 and 0 in place of 1)

we have implemented the above logic but it takes lot of recursion depth . 

for alter solution 

after observing the data again and condition 

previous values act as first half of next value and inverse values act as second half 

for if given row or n as 5 , and k as some values

if K position is > half position of row , 
    then k position of previous row will be  at K position - half value as the same position row of prevoius row
    and value will be inversed
if k position is <= half , it takes same value

in logic I have taken a helper value, that value will be inversed if k is greated than half else same value

tried helper value intial with 0 and 1 , 0 worked well where if we take 1 we have to inverse final value

'''