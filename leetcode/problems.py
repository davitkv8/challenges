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

    def zigzag_conversion(self, s, row_num):

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

    # 1, 10, 13, 19, 22, 31, 34, 55, 57  |  8, 36
    def findMedianSortedArrays(self, nums1, nums2):

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


solution = Solution()

print(
    solution.findMedianSortedArrays([1, 2], [3, 4])
)
