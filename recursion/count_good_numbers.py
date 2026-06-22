
'''
logic for below code.

as per problem statement 
a number is good number 
if the even positions (starting from left with 0 as index) are even number
and odd postion numbers are prime.

that is even numbers [2,4,6,8,0] are 5 numbers
and prime numbers are [2,3,5,7] are 4 number

if n=1
i,e  _ ---> position 0
then good numbers are even number and count is 5

if n= 2

    _ _ 
    | |
    | |----> postion 1 from left takes prime number as odd positon. 4 prime number
    |------>position 0 from left takes even number as even postion takes 5 even numbers

    total good number are 4X5 = 20

if n=3
    _ _ _
    | | |----> position 2 from left takes even number as even postion takes 5 even numbers
    | |----> postion 1 from left takes prime number as odd positon. 4 prime number
    |------>position 0 from left takes even number as even postion takes 5 even numbers

    
    total good number are 5X4X5 = 100


if n=4
    _ _ _ _ --> postion 3 from left takes prime number as odd positon. 4 prime number
    | | |----> position 2 from left takes even number as even postion takes 5 even numbers
    | |----> postion 1 from left takes prime number as odd positon. 4 prime number
    |------>position 0 from left takes even number as even postion takes 5 even numbers

    
    total good number are 5X4X5X4 = 400

if you see the pattern here it is 
if n=1 (odd) ; result is 5
if n=2 (even); result is 5^1 X 4^1 = 20
if n=2 (odd) ; result is 5^2 X 4^1 = 100
if n=2 (even); result is 5^2 X 4^2 = 400
if n=2 (odd) ; result is 5^3 X 4^2 = 2000

so if n is even answer is 5^(n/2) X 4^(n/2)
   if n is odd  answer is 5^((n/2)+1) X 4^(n/2)

the problem arised with larger number more than 10K 

'''


def countGoodNumbers(n: int) -> int:

    init_val=2

    def helper(expo, req_n):
        if expo==n:
            return expo
        if expo>req_n : 
            return helper(expo//2,req_n - (expo//2))
        expo*=expo
        return helper(expo,n)
    return helper(init_val,n)


print(countGoodNumbers(255)) 

    # if n %2 ==0 : 
    #     m=n//2
    #     return (5**m) * (4**m) if (5**m)*(4**m)<((10**9)+7) else (5**m)*(4**m)% ((10**9)+7)
    # else:
    #     m=n//2
    #     return 5*(5**m)*(4**m) if 5*(5**m)*(4**m)<((10**9)+7) else 5*(5**m)*(4**m)% ((10**9)+7) 


