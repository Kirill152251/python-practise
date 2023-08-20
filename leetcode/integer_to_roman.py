# Problem content:
# https://leetcode.com/problems/integer-to-roman/

# x % 10 - последняя цифра числа
# x // 10 - отрезать от числа х крайнюю цифру справа (младший разряд)

class Solution:

    @staticmethod
    def base(num: int, low: str, high: str, super_high: str) -> str:
        b = {1: low, 2: low * 2, 3: low * 3, 4: low + high, 5: high, 6: high + low, 7: high + low * 2,
             8: high + low * 3, 9: low + super_high, 0: ''}
        return b[num]

    def int_to_roman(self, num) -> str:
        u = num % 10
        num = num // 10
        d = num % 10
        num = num // 10
        h = num % 10
        num = num // 10
        th = num % 10
        return self.base(th, 'M', '', '') + self.base(h, 'C', 'D', 'M') + \
            self.base(d, 'X', 'L', 'C') + self.base(u, 'I', 'V', 'X')

    @staticmethod
    def int_to_roman_gs(num) -> str:
        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V", 4: "IV",
            10: "X", 9: "IX",
            50: "L", 40: "XL",
            100: "C", 90: "XC",
            500: "D", 400: "CD",
            1000: "M", 900: "CM",
        }

        # Result Variable
        r = ''

        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num -= n
        return r
