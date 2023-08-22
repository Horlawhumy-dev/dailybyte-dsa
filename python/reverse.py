class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        reversed_str  = list()
        is_less_than_zero = True if x < 0 else False

        x = -1 * x if is_less_than_zero else x

        while x > 0:

            rem = x % 10

            reversed_str.append(str(rem))
            #take care of given 120 => 021 => 21
            if reversed_str[0] == "0":
                reversed_str.pop()
            
            x //= 10
        
        

        x = int("".join(reversed_str))
        x = (-1 * int(x)) if is_less_than_zero else int(x)
        #take care of boundary of -2**31 to 2**31-1 for 32bits
        if x < -2**31 or x > (2**31-1):
            return 0

        return x
