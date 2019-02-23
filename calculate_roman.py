import unittest


def roman_to_decimal(roman):
    R2D_MAP = {'I' :1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000,
           'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

    i = 0
    decimal_sum = 0
    while i < len(roman):
        print(f"****current i: {i}, roman[i]: {roman[i]}****")
        if roman[i] not in R2D_MAP and roman[i].upper() not in R2D_MAP:
            return -1

        if i+1 < len(roman):
            current_char = roman[i].upper()
            next_char = roman[i+1].upper()
            if R2D_MAP[next_char] <= R2D_MAP[current_char]:
                decimal_sum += R2D_MAP[roman[i]]
                print(f"i:{i}, roman[i]: {current_char}, decimal_sum:{decimal_sum}")
                i += 1
            else:
                if current_char == 'C':
                    if next_char == 'D':
                        decimal_sum += 400
                    else:
                        decimal_sum += 900

                elif current_char == 'X':
                    if next_char == 'L':
                        decimal_sum += 40
                    else:
                        decimal_sum += 90
                elif current_char == 'I':
                    if next_char == "V":
                        decimal_sum += 4
                    else:
                        decimal_sum += 9
                print(f"i:{i}, roman[i]: {current_char}, decimal_sum:{decimal_sum}")
                i += 2
        else:
            ## it is the last letter
            decimal_sum += R2D_MAP[roman[i].upper()]
            return decimal_sum

    return decimal_sum

class TestCalculateRoman(unittest.TestCase):
    def test1(self):
        self.assertEqual(roman_to_decimal('I'),1)

    def test2(self):
        self.assertEqual(roman_to_decimal('XI'),11)

    def test3(self):
        self.assertEqual(roman_to_decimal('MCMXCVIII'),1998)
    #
    def test4(self):
        self.assertEqual(roman_to_decimal('MMMCMXCIX'),3999)


if __name__ == "__main__":
    unittest.main()