from collections import deque
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        queue = deque([])
        temp = x
        while temp > 0:

            queue.appendleft(temp%10)

            temp //= 10

        palindrome = 0
        power = 0

        while queue:

            val = queue.popleft()

            palindrome += val * 10**power

            power += 1

        temp = x
        palindrome = 0
        power = 0
        while temp > 0:

            palindrome += (temp % 10) * 10**power

            temp //= 10
            power += 1

        
        return palindrome == x