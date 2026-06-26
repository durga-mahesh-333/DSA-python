
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
if n=4 (odd) ; result is 5^2 X 4^1 = 100
if n=5 (even); result is 5^2 X 4^2 = 400
if n=6 (odd) ; result is 5^3 X 4^2 = 2000

so if n is even answer is 5^(n/2) X 4^(n/2)
   if n is odd  answer is 5^((n/2)+1) X 4^(n/2)

the problem arised with larger number more than 10K 

to further simplyfy it 
if even 
    5^(n/2) X 4^(n/2)
    = 20^(n/2)
    = 2^(n/2) X 10^(n/2)

if odd 
    2^(n/2) X 10^(n/2) X 5

here we gonna apply pow of 2 logic 

'''


def countGoodNumbers(n: int) -> int:
    modulo_val=(10**9) + 7
    pow_ten_multple = pow(10,n//2,modulo_val) if n>9 else (10**(n//2))
    #(10**(n//2))%modulo_val if n>9 else (10**(n//2))
    def helper(expo, base):
        if expo == 0:
            return 1 
        updat_val=helper(expo//2,base)    
        if updat_val>modulo_val:
            updat_val%=modulo_val
        final_val= updat_val*updat_val if expo%2==0 else updat_val*updat_val*2
        return final_val if final_val<modulo_val else final_val%modulo_val
    # req_value= helper(n//2,2)*(10**(n//2))*(5 if n%2==1 else 1)
    req_value= helper(n//2,2)*pow_ten_multple
    return req_value if req_value < modulo_val else req_value%modulo_val


print(countGoodNumbers(50)) 

    # if n %2 ==0 : 
    #     m=n//2
    #     return (5**m) * (4**m) if (5**m)*(4**m)<((10**9)+7) else (5**m)*(4**m)% ((10**9)+7)
    # else:
    #     m=n//2
    #     return 5*(5**m)*(4**m) if 5*(5**m)*(4**m)<((10**9)+7) else 5*(5**m)*(4**m)% ((10**9)+7) 


