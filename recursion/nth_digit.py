def findNthDigit(n: int) -> int:
    if n < 10 : return n

    def recur_helper(ten_pow, total_digits_count , prev_total_digits_count):
        total_digits_count+= 9 * (10**ten_pow) * (ten_pow+1)
        if total_digits_count > n :
            return prev_total_digits_count,ten_pow
        return recur_helper(ten_pow+1, total_digits_count , prev_total_digits_count=total_digits_count)

    digit_value , digit_count= recur_helper(1, 9 , 0)

    return digit_value,(digit_value+ n//digit_count +n%digit_count) , (digit_value+ n//digit_count +n%digit_count)%(10*digit_count)

print(findNthDigit(189))
