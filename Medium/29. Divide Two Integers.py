class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # edge case overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # tentuin tanda
        negative = (dividend < 0) != (divisor < 0)

        # kerja pakai positif biar aman
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # doubling
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        return -result if negative else result
