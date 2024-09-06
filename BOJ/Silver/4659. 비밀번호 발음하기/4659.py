import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']


def check_vowel(string):
    for vowel in vowels:
        if vowel in string:
            return 1

    return 0


def check_double(string):
    for i in range(1, n):
        if string[i] == string[i - 1] and string[i] not in {'e', 'o'}:
            return 0

    return 1


def check_triple(string):
    for i in range(2, n):
        vowel, consonant = 0, 0
        for alp in string[i - 2:i + 1]:
            if alp in vowels:
                vowel += 1

            else:
                consonant += 1

        if 3 in {vowel, consonant}:
            return 0

    return 1


while 1:
    string = input().rstrip()
    if string == 'end':
        break

    n = len(string)
    result = 'is acceptable.'
    if not check_vowel(string) or not check_double(string) or not check_triple(string):
        result = 'is not acceptable.'

    print(f'<{string}>', result)
