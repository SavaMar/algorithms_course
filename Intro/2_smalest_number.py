# def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

# my solution
def smallest_positive(in_list):
    in_list.sort()
    for i in in_list:
        if i >= 0:
            return i

# solution
# def smallest_positive(in_list):
#     smallest_pos = None
#     for num in in_list:
#         if num > 0:
#             if smallest_pos == None or num < smallest_pos:
#                 smallest_pos = num
#     return smallest_pos