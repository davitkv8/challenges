# romanToInt

class Solution:

    roman_characters = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    def roman_to_int(self, s):
        """
            :type s: str
            :rtype: int
        """

        index = 0
        result = 0
        while index < s.__len__():
            try:
                if self.roman_characters.get(s[index]) >= self.roman_characters.get(s[index + 1]):
                    result += self.roman_characters.get(s[index])
                else:
                    result -= self.roman_characters.get(s[index])
            except IndexError:
                result += self.roman_characters.get(s[index])

            index += 1

        return result

    def length_of_longest_substring(self, s):

        substring = ""
        max_length = 0
        for char in s:
            if char in substring:
                char_index = substring.index(char)
                substring = substring[(char_index+1):]

            substring += char
            max_length = max(
                max_length, len(substring)
            )

        return max_length

    def convert(self, s, row_num):

        if row_num == 1 or row_num > s.__len__():
            return s

        starter = 0
        plus = True

        row_num_dimensional_array = [""] * row_num

        for i in s:
            row_num_dimensional_array[starter] += i

            if starter == 0:
                plus = True

            if starter < row_num - 1 and plus:
                starter += 1
            else:
                starter -= 1
                plus = False

        row_num_dimensional_array = ''.join(row_num_dimensional_array)

        return row_num_dimensional_array


solution = Solution()
print(solution.convert("!@#%^&*()", 6))
