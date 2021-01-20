
def convert(num,b):
    rem = num%b
    if (rem>=10):
        rem = chr(rem + 55)
    if (num<=1): 
        return str(num)
    else:
        return str(convert(num//b,b)) + str(rem)
