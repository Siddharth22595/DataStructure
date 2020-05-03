# Given a string, you need to find longest substring having only unique characters.
# For example, str = "ABCBCDE". the ans is bcde with len = 4


def fun(string):
    a_to_z_string = "abcdefghijklmnopqrstuvwxyz"
    initial_chars_dict = dict()
    for i in range(len(a_to_z_string)):
        initial_chars_dict[a_to_z_string[i]] = True
    print("initial_chars_dict --> %s", str(initial_chars_dict))
    answer_dict = dict()
    for i in range(len(string)):
        longest_substring = str()
        longest_substring_length = 0
        chars_dict = dict()
        print("chars_dict --> %s", str(chars_dict))
        for j in range(i, len(string)):
            if string[j] not in chars_dict.keys():
                chars_dict[string[j]] = True
            if chars_dict[string[j]] is True:
                longest_substring = longest_substring + string[j]
                longest_substring_length += 1
                chars_dict[string[j]] = False
            else:
                break
        answer_dict[longest_substring] = longest_substring_length
        print("answer_dict --> %s", str(answer_dict))
    longest_substring = max(answer_dict, key=answer_dict.get)
    return longest_substring


input_string = "abcdefghijklmnopqrstuvwxyza"
output_string = fun(input_string)
print("output_dict --> %s", output_string)

