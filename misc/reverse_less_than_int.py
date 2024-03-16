def reverse(x: int) -> int:
    if x==0:
        return 0
    n = abs(x)
    sign = x//n
    rev=0
    int_min = -2**31
    int_max = 2**31-1
    while n>0:
        rev = rev*10 + (n%10)
        if (rev*sign)< int_min or (rev*sign)>int_max:
            return 0
        n=n//10
    return rev*sign
print(reverse(-34))