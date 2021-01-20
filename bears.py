def bears(n):
    if n == 42: 
        return True
    elif n < 42: 
        return False
    else:
        nums = [0, 0, 0]
        if n % 2 == 0: 
            nums[0] = n // 2
        if n % 3 == 0 or n % 4 == 0:
           last = n % 100
           ones = last % 10 
           tens = last // 10
           if ones == 0 or tens == 0:
               nums[1] = 0
           else:
               nums[1] = n - (ones * tens)
        if n % 5 == 0:
            nums[2] = n - 42
        for num in nums: 
            if bears(num) is True:
                return True

             
