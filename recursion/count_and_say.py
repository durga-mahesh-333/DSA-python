def countAndSay(n: int) -> str:
    if n ==1 : return '1'
    if n==2 : return '11'
    start_string='11'
    def compression_logic(input_string):
        count=1
        prev_str=''
        curr_str=''
        updt_str=''
        for i in range(len(input_string)-1,-1,-1): #11
            curr_str=input_string[i]
            # if i last element from the right , it is first element from left
            if i==0 :          
                if len(input_string)==1:
                    return str(count)+curr_str  
                if prev_str==curr_str:
                    return str(count+1)+curr_str+updt_str
                else:
                    return str(1)+curr_str+str(count)+prev_str+updt_str
                
            #if i is the first element for the calcualtion , then it is last from the right  as we are doing the logic from right
            elif i==len(input_string)-1:
                pass
            else:
                if curr_str==prev_str:
                    count+=1
                else:
                    updt_str=str(count)+prev_str+updt_str
                    count=1
            prev_str=curr_str

        return updt_str

    def helper(incr_num, updt_str):
        if incr_num==n:
            return updt_str
        new_updt_str=compression_logic(updt_str)
        return helper(incr_num+1, new_updt_str)
    
    return helper(2,start_string)
# num=4
# for i in range(1,num+1):
#     print(countAndSay(i))
print(countAndSay(8))