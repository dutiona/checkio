def has_line(game_result):
    for l in game_result:
        if l == tuple("XXX"):
            return "X"
        elif l == tuple("OOO"):
            return "O"
    return None

def has_col(game_result):
    return has_line(zip(*[list(e) for e in game_result]))

def has_diag(game_result):
    def check_diag(c, reverse=False) :
        for i in range(len(game_result)):
            if (not reverse and game_result[i][i] != c) or \
                (reverse and game_result[i][len(game_result) - 1 - i] != c):
                return False
        return True
    return "X" if check_diag("X") or check_diag("X", reverse=True) else "O" if check_diag("O") or check_diag("O", reverse=True) else None

def checkio(game_result):
    line = has_line([tuple(e) for e in game_result])
    col = has_col(game_result)
    diag = has_diag(game_result)
    return line if line is not None else col if col is not None else diag if diag is not None else "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    assert checkio(["X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio(["OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio(["OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio(["O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

