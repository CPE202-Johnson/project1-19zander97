
def convert(num,b):
    rem = num%b
    if (rem>=10):
        rem = chr(rem + 55)
    if (num==0): 
        return str()
    else:
        return str(convert(num//b,b)) + str(rem)
