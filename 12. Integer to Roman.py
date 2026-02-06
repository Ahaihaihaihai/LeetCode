class Solution(object):
    def intToRoman(self, num):
        roman = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        if num in roman:
            return roman[num]
        ans = ""
        counter = 1

        while num > 0:
            digit = num % 10

            if digit == 4:
                ans = roman[counter] + roman[counter*5] + ans
            elif digit == 9:
                ans = roman[counter] + roman[counter*10] + ans
            elif digit >= 5:
                ans = roman[counter*5] + roman[counter] * (digit - 5) + ans
            else:
                ans = roman[counter] * digit + ans

            num //= 10
            counter *= 10

        return ans

        
x = Solution()
print(x.intToRoman(1010))

