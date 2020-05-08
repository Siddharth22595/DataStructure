# Given a string, you need to find longest substring having only unique characters.
# For example, str = "ABCBCDE". the ans is bcde with len = 4

# -- O(n) approach


def fun(input_string):
    """O(n) approach"""
    a_to_z_string = "abcdefghijklmnopqrstuvwxyz"
    initial_chars_dict = dict()
    for i in range(len(a_to_z_string)):
        initial_chars_dict[a_to_z_string[i]] = 0
    print("initial_chars_dict --> " + str(initial_chars_dict))
    longest_substring = str()
    length = 0
    output_dict = dict()
    for i in range(len(input_string)):
        if initial_chars_dict[input_string[i]] == 0:
            initial_chars_dict[input_string[i]] = 1
            longest_substring = longest_substring + input_string[i]
            length = length + 1
        else:
            # assigning all the elements as 0
            initial_chars_dict.update(initial_chars_dict.fromkeys(initial_chars_dict.keys(), 0))
            initial_chars_dict[input_string[i]] = 1
            longest_substring = input_string[i]
            length = 1
        output_dict[longest_substring] = length
        print("output_dict --> %s", str(output_dict))
    return max(output_dict, key=output_dict.get)


input_string = "abcbcdeefghijkl"
output_string = fun(input_string)
print("output_string --> %s", output_string)

# Below is O(n^2) approach
# def fun(string):
#     a_to_z_string = "abcdefghijklmnopqrstuvwxyz"
#     initial_chars_dict = dict()
#     for i in range(len(a_to_z_string)):
#         initial_chars_dict[a_to_z_string[i]] = True
#     print("initial_chars_dict --> %s", str(initial_chars_dict))
#     answer_dict = dict()
#     for i in range(len(string)):
#         longest_substring = str()
#         longest_substring_length = 0
#         chars_dict = dict()
#         print("chars_dict --> %s", str(chars_dict))
#         for j in range(i, len(string)):
#             if string[j] not in chars_dict.keys():
#                 chars_dict[string[j]] = True
#             if chars_dict[string[j]] is True:
#                 longest_substring = longest_substring + string[j]
#                 longest_substring_length += 1
#                 chars_dict[string[j]] = False
#             else:
#                 break
#         answer_dict[longest_substring] = longest_substring_length
#         print("answer_dict --> %s", str(answer_dict))
#     longest_substring = max(answer_dict, key=answer_dict.get)
#     return longest_substring
#
#
# input_string = "abcdefghijklmnopqrstuvwxyza"
# output_string = fun(input_string)
# print("output_dict --> %s", output_string)


