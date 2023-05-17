from pprint import pprint as pp
from helpers import *

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


def merge_the_tools(string, k):

    if string.__len__() % k:
        return

    count = 1

    unique_chars = ""
    while count <= string.__len__():
        if string[count - 1] not in unique_chars:
            unique_chars += string[count - 1]

        if count % k == 0:
            print(unique_chars)
            unique_chars = ""

        count += 1


def find_angle(ab, bc):
    import math

    mc = math.sqrt(ab ** 2 + bc ** 2)

    result = round(
        math.degrees(math.acos(bc / mc))
    )

    print(f"{result}{chr(0xB0)}")


def triangle_quest(n):
    for i in range(1, n + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print((10 ** i - 1) ** 2 // 81)


# Day dd Mon yyyy hh:mm:ss +xxxx
def time_delta(t1, t2):

    utc_regex = {
        1: "M",
        2: "MM",
        3: "HMM",
        4: "HHMM"
    }

    extract_timezone = lambda t: t.split(" ")[-1]
    utc_timezone1, utc_timezone2 = extract_timezone(t1), extract_timezone(t2)

    extract_date = lambda t: t.split(" ")[1]
    date1, date2 = extract_date(t1), extract_date(t2)

    extract_time = lambda t: t.split(" ")[4]
    time1, time2 = extract_time(t1), extract_time(t2)

    utc_difference = str(abs(int(utc_timezone1) - int(utc_timezone2)))

    utc_difference_in_hour = calculate_with_regex(utc_regex, utc_difference)

    split_times = lambda t: t.split(":")
    time1 = split_times(time1)
    time2 = split_times(time2)

    minus_times = list(
        map(lambda x, y: str(int(x) - int(y)), time1, time2)
    )

    time_difference_in_hour = calculate_with_regex(utc_regex, ''.join(minus_times))
    time_difference_with_utc = time_difference_in_hour - utc_difference_in_hour
    date_difference = (int(date1) - int(date2)) * 24

    full_diff_in_sec = abs(
        int((date_difference + time_difference_with_utc) * 3600)
    )

    return full_diff_in_sec



if __name__ == '__main__':


    time_delta(
        t1="Sun 10 May 2015 13:54:36 -0700",
        t2="Sun 10 May 2015 13:54:36 -0000"
    )
