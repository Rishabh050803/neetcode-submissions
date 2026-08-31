class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            total = 0
            temp = n
            while temp:
                total += (temp%10)**2
                temp = temp//10
            # print(total)
            if total == 1:
                return True
            if total in seen:
                return False
            seen.add(total)
            n = total