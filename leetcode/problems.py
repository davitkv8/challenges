from double_linked_list import DoubleLinkedList


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

    def find_median_sorted_arrays(self, nums1, nums2):

        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a

        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            a_left = a[i] if i >= 0 else float("-infinity")
            a_right = a[i + 1] if (i + 1) < len(a) else float("infinity")
            b_left = b[j] if j >= 0 else float("-infinity")
            b_right = b[j + 1] if (j + 1) < len(b) else float("infinity")

            # partition is correct
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2:
                    return min(a_right, b_right)
                # even
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1

    def reverse_nodes_in_k_group(self, values_list, k):

        my_linked_list = DoubleLinkedList()

        for value in values_list:
            my_linked_list.append(value)

        my_linked_list.reverse_nodes_in_k_group(k)

        return my_linked_list.convert_to_list()


solution = Solution()
