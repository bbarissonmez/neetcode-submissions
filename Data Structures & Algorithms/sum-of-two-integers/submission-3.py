class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry_in = 0

        for i in range(32):
            a_bit = 1 & (a >> i)
            b_bit = 1 & (b >> i)

            xor = a_bit ^ b_bit
            carry_out = a_bit & b_bit | (carry_in) & (a_bit ^ b_bit)

            if (carry_in == 1):
                xor = 1 - xor

            res |= (xor << i)
            carry_in = carry_out

        return res if res < (1 << 31) else res - (1 << 32)


