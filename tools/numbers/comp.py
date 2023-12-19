from icecream import ic


#  gets a number and returns sum of digits
def sumofdigits(num):
    str_number = str(num)
    digit_sum = 0
    for digit_str in str_number:
        digit_sum += int(digit_str)
    
    return digit_sum

#  return True if the number is palindrome 
def ispal(num):
    str_number = str(num)
    return str_number == str_number[::-1] 

