def findTheWinner( n: int, k: int) -> int:
    if k==1 or n==1 : return n
    list_from_input=[i+1 for i in range(0,n) ]
    def helper(reordered_list):
        if len(reordered_list)==1:
            return reordered_list[0]
        
        updated_counter = k%len(reordered_list) if k> len(reordered_list) else k
        
        if not updated_counter : updated_counter=len(reordered_list)
        updated_reordered_list=reordered_list[updated_counter:]+reordered_list[:updated_counter-1]
        return helper(updated_reordered_list)
    return helper(list_from_input)

print(findTheWinner(7,8))

'''
explaination for above code:

take the number of people (n) in a list -> eg : [1,2,3,4,5,6,7]

for each loop we check k greated that no of people , 
if k greater then we do remainder division to reduce no of count, example
    if k= 10 in above scenario, if we count ten round the people , tenth count stops at 3
    if we do remainder division with no of people i.e 10%7 = 3 , so we count 3 from start of the loop 
    it is applicable for every loop 

rather than taking circular linked list an remove , we used simnple list and once we get updated k or k , 
we rearrange the list in a way that next person would be start of count (i.e start of list ) and before people of number will go to end of list like below)

[1,2,3,4,5,6,7] k=10

count stops at 3 (up_k) or up_k=10%7 =3 (as k greater that num of people else we might have take k only)
[1 , 2 ] ,      3   , [4,5,6,7,8]

[:(up_k-1)] , up_k  , [ up_k : ]

[ up_k : ] + [:(up_k-1)]

[4,5,6,7,8] + [1,2]

[4,5,6,7,8,1,2]

now in the next loop count starts from start of list (which is person after deleted person)
and updated k caluclation is follows same and so on

'''