import re

def checkio(text):
    lst = filter(lambda l : not re.match("[^a-zA-Z]", l), list(text))
    lst = list(map(lambda l: l.lower(), lst))
    lst.sort()
    max_nb = 1
    max_letter = lst[0]
    current_nb = max_nb
    current_letter = max_letter
    for l in lst[1:]:
        if current_nb > max_nb:
            max_letter = current_letter
            max_nb = current_nb

        if l == current_letter:
            current_nb += 1
        else:
            current_letter = l
            current_nb = 1

    return max_letter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
