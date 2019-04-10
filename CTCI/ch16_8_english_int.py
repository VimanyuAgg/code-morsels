def numberToWords(num: int) -> str:
    ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    hundred = " Hundred"
    bigs = ["", " Thousand", " Million", " Billion"]
    negative = "Negative "

    def _convertToEnglish(n, counter):
        if n == 0 and counter == 0:
            return ones[0]
        elif n == 0:
            return ""

        res = ""
        if n % 1000 > 0:
            res = _handleTill99(n % 1000) + bigs[counter]

        prefix = _convertToEnglish(n // 1000, counter + 1)
        if prefix != "" and res != "":
            prefix += " "

        return prefix + res

    def _handleTill99(val):
        h = val // 100
        res = ""
        if h > 0:
            res += ones[h] + hundred

        if val % 100 == 0:
            return res

        elif val % 100 > 19:
            if res != "":
                res += " "

            tens_digit = (val % 100) // 10
            if tens_digit == 0:
                return res + ones[val % 10]
            else:
                unit_digit = "" if val % 10 == 0 else " " + ones[val % 10]
                return res + tens[tens_digit] + unit_digit

        else:
            if res != "":
                res += " "
            return res + ones[val % 100]

    if num >= 0:
        return _convertToEnglish(num, 0)
    else:
        return negative + _convertToEnglish(-num, 0)