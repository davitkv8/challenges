from pprint import pprint as pp


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# String = BANANA
def minion_game(string):
    vowels = ('A', 'E', 'I', 'O', 'U')

    kevin_score, stuart_score = 0, 0

    index = 0

    while index < string.__len__():

        current_char = string[index]

        if current_char in vowels:
            kevin_score += string.__len__() - index
        else:
            stuart_score += string.__len__() - index

        index += 1

    if stuart_score == kevin_score:
        return "Draw"

    elif stuart_score > kevin_score:
        return f"Stuart {stuart_score}"

    else:
        return f"Kevin {kevin_score}"


if __name__ == '__main__':
    s = input()
    print(minion_game(s))
