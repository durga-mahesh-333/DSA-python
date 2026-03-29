
# def kthGrammar( n: int, k: int) -> int:
#     if n==1 and k==1: return 0
#     helper_str=''
#     if n>=2 : helper_str='01'
        
#     def second_part_gen(str_val:str , index:int , req_part:str):
#         if index==len(str_val):
#             return req_part
#         req_part+=str(1-int(str_val[index]))
#         return second_part_gen(str_val , index+1 , req_part)
#     def helper(row_val:int , final_str:str):
#         if row_val==n:
#             return final_str
#         if (row_val)%2==1: 
#             sec_part=second_part_gen(final_str , 0 , '')
#             print(f'row_value:{row_val}, sec_part from not :{sec_part}')
#         else : 
#             sec_part= final_str[::-1]
#             print(f'row_value:{row_val}, sec_part from rev :{sec_part}')
#         req_str=final_str+sec_part
#         # print(f'second_part : {sec_part}  ')
#         return helper(row_val+1 , req_str)

#     kth_val= helper(2,helper_str)#[k-1]
#     return kth_val

# print(kthGrammar(7,5))

print(bin(30))#.count('1'))
'''
n=2 01
n=3 0110
n=4 01101001
n=5 0110100110010110
n=6 01101001100101101001011001101001
n=7 0110100110010110100101100110100110010110011010010110100110010110

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




'''