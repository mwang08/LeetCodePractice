# roman Integer


def romanToInt(s: str) -> int:
    symbol_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def check_later_char(first_char, second_char):
        if first_char == 'I':
            if second_char == 'V' or second_char == 'X':
                return True
            else:
                return False
        if first_char == 'X':
            if second_char == 'L' or second_char == 'C':
                return True
            else:
                return False
        if first_char == 'C':
            if second_char == 'D' or second_char == 'M':
                return True
            else:
                return False

    result = 0
    for i in range(len(s)):
        char = s[i]

        try:
            next_char = s[i + 1]
            if check_later_char(char, next_char):
                result += -1 * symbol_value[char]
            else:
                result += symbol_value[char]
        except:
            result += symbol_value[char]

    return result


romanToInt('IV')