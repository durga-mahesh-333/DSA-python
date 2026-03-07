from typing import List


def reverseString(s: List[str]) -> None:
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    def reverse(swap_index1:int , swap_index2:int):
        if swap_index1>=swap_index2:
            return
        s[swap_index1],s[swap_index2]=s[swap_index2],s[swap_index1]
        reverse(swap_index1+1,swap_index2-1)
    reverse(0,len(s)-1)
        
test_str=['h','e','l','l','o']
reverseString(test_str)
print(test_str)
        