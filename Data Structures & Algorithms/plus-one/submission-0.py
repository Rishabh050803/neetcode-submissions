class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        # print(digits)
        carry = 1
        for i,x in enumerate(digits):
            digits[i] = (x+carry)%10
            carry = (carry+x)//10
        if carry:
            digits.append(carry)
        
        digits.reverse()
        return digits
