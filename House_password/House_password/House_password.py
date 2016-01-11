def checkio(data):
    if len(data) < 10:
        return False

    has_capital = False
    has_normal = False
    has_number = False
    for letter in data:
        if has_normal or letter >= 'a' and letter <= 'z': has_normal = True
        if has_capital or letter >= 'A' and letter <= 'Z': has_capital = True
        if has_number or letter >= '0' and letter <= '9': has_number = True
   
    return has_capital and has_normal and has_number

#Some hints
#Just check all conditions

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
