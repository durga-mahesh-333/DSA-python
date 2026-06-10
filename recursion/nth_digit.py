def findNthDigit(n: int) -> int:
    if n < 10 : return n

    def recur_helper(no_of_digits,  current_incr_value ):
        print(f'ten_pow:{no_of_digits} , current_incr_value:{current_incr_value}')
        prev_incr_value=current_incr_value
        num_of_digits_after_prev_num=no_of_digits+1 #number of digits for each number after prev_incr_value
        current_incr_value=prev_incr_value+(9*(10**no_of_digits)*(num_of_digits_after_prev_num))
        print(f'current_incr_value after cal :{current_incr_value}')
        if current_incr_value > n : 
            return prev_incr_value, num_of_digits_after_prev_num #no of digits for each number in 
        return recur_helper(no_of_digits+1,current_incr_value)
    max_digit_count_of_prev_digit_count , digit_count_for_each_num  = recur_helper(1,  9 )

    prev_digit_count= digit_count_for_each_num-1
    max_num_for_prev_digit_count= 10**prev_digit_count-1
    no_of_digits_in_curr_digit_count = n-max_digit_count_of_prev_digit_count
    final_num_with_leftover_digits = max_num_for_prev_digit_count+ \
                                            (no_of_digits_in_curr_digit_count//digit_count_for_each_num) 
    left_over_digits = no_of_digits_in_curr_digit_count%digit_count_for_each_num

    final_numer_to_check=final_num_with_leftover_digits + (1 if left_over_digits else 0)

    return int(str(final_numer_to_check)[left_over_digits-1])



print(findNthDigit(146))


# prev_incr_value+(prev_incr_value*(10**ten_pow)*2)
# 9+9*(10^1)*2
# 189+9*(10^2)*(3)  =   2889
# 2889+9*(10^3)*(4) =  38889