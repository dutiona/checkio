FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    lst = []
    if number % 100 < 20 and number % 100 > 0:
        lst.append((FIRST_TEN + SECOND_TEN)[number % 20 - 1])
        number -= number % 20
    if number % 100 != 0:
        if number % 10 != 0:
            lst.append(FIRST_TEN[number % 10 - 1])
            number -= number % 10
        lst.append(OTHER_TENS[int(number % 100 / 10) - 2])
        number -= number % 100
    if number % 1000 != 0:
        lst.append(HUNDRED)
        lst.append(FIRST_TEN[int(number % 1000 / 100) - 1]) 
    lst.reverse()
    return ' '.join(lst)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
