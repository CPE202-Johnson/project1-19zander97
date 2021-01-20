
def convert(num,b):
   char = "0123456789ABCDEF"  
   if num < b: return char[num]
   else:
      return convert(num//b,b) + char[num % b]
