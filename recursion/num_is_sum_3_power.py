def checkPowersOfThree( n: int) -> bool:
    if n==1:
        return True
    if n==2 or n%3==2 :
        return False
    n=n//3
    return checkPowersOfThree( n )

print(checkPowersOfThree( 11 ))


'''
logic : 

some where from comments I have read that use just like binary calculation , instead 2 of use 3

if we take 91 
    we will get binary calulation with base 3 as below

    1   0   1   0   1
    3^4 3^3 3^2 3^1 3^0

    (1*3^4)+(1*3^2)+(1*3^0) = 81+9+1 = 91
    This condition satisfies as True

for value 21
    2   1   0
    3^2 3^1 3^0

    (2*3^2)+(1*3^1) = 18+3 = 21
    this false as we got 2 in the calcualtion of binary number with base three

for value 11
    last remainder is 2 , here it is also false \
    s
using above conditions , we have written code


'''