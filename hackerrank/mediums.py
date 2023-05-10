from pprint import pprint as pp


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# String = BANANA
def minion_game(string):
    str_to_upper = string.upper()
    vowels = ('A', 'E', 'I', 'O', 'U')

    players = {
        "Stuart": {
            "vowels": False,
            "score": 0
        },

        "Kevin": {
            "vowels": True,
            "score": 0
        }
    }

    for player in ['Stuart', 'Kevin']:

        vowel_condition = players[player]['vowels']

        possible_substrings = {

        }

        index = 0

        while index < str_to_upper.__len__():

            current_char = str_to_upper[index]

            if (current_char in vowels) == vowel_condition:

                index_substring = index

                while index_substring < str_to_upper.__len__():

                    substring = str_to_upper[index: index_substring + 1]

                    # Just for visualisation which substring were repeated how many times
                    # This will decrease time complexity. just delete it if don't needed.

                    if possible_substrings.get(substring):
                        possible_substrings.update({
                            substring: possible_substrings.get(substring) + 1
                        })

                    else:
                        possible_substrings.update({
                            substring: 1
                        })

                    index_substring += 1
                    players[player]['score'] += 1

            index += 1
        # pp(possible_substrings)
        print("|_________________________________________________________|")

    # pp(players)

    results = list(i['score'] for i in players.values())

    if results[0] is results[1]:
        return "Draw"

    winner = max(players, key=lambda user: players[user]['score'])

    return f"{winner} {players.get(winner)['score']}"


if __name__ == '__main__':
    s = input()
    print(minion_game(s))
