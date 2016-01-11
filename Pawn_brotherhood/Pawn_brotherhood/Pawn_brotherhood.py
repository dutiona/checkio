def safe_pawns(pawns):
    letters = tuple("abcdefgh")
    numbers = dict(zip(letters, range(0, 8)))
    protected_area = []
    for pawn in pawns:
        l = numbers[pawn[0]]
        n = int(pawn[1])
        if n < 8:
            if l > 0:
                protected_area.append(letters[l - 1] + str(n + 1))
            if l < 7:
                 protected_area.append(letters[l + 1] + str(n + 1))
    return len(list(filter(lambda e: protected_area.count(e) > 0, pawns)))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
