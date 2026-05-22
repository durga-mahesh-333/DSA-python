def lastRemaining( n: int, recur_count) -> int:
    if n==1: return 1
    intial_list_after_first_removal=[i for i in range(2,n+1,2)]
    def helper(list_data, count):
        new_list=[]
        if count==recur_count:
            return list_data
        if len(list_data)==1:
            return list_data[0]
        for i in range(len(list_data)-2,-1,-2):
            new_list.append(list_data[i])
        return helper(new_list,count+1)
    return helper(intial_list_after_first_removal,2)

print(lastRemaining(30,3))


'''#Brute solution 
def lastRemaining( n: int) -> int:
    if n==1: return 1
    intial_list=[i for i in range(1,n+1)]

    def removal_recursion(data_list):
        new_list=[]
        if len( data_list )==1:
            return data_list[0]
        for i in range(1,len(data_list)+1):
            if i%2==0:
                new_list.append(data_list[i-1])
        return removal_recursion(new_list[::-1])
    return removal_recursion(intial_list)'''
        