
def kthGrammar( n: int, k: int) -> int:
    if n==1 and k==1: return 0
    helper_str=''
    if n>=2 : helper_str='01'
        
    def second_part_gen(str_val:str , index:int , req_part:str):
        if index==len(str_val):
            return req_part
        req_part+=str(1-int(str_val[index]))
        return second_part_gen(str_val , index+1 , req_part)
    def helper(row_val:int , final_str:str):
        if row_val==0:
            return final_str
        sec_part=second_part_gen(final_str , 0 , '')
        req_str=final_str+sec_part
        # print(f'second_part : {sec_part}  ')
        return helper(row_val-1 , req_str)

    kth_val= helper(n-2,helper_str)#[k-1]
    return int(kth_val)

print(kthGrammar(6,5))


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


'''