# for string
user_input = input("Enter a string: ")
def swap_first_last_string(s):
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]

result = swap_first_last_string(user_input)

print("After swapping first and last characters:", result)


# for list
user_input = input("Enter elements of the list separated by space: ")
def swap_first_last_list(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

lst = list(map(int, user_input.split()))
result = swap_first_last_list(lst)

print("After swapping first and last:", result)
