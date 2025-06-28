# questions

#FiboNacci Series

n = int(input("Enter Number = "))

def fibonaci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonaci(n)


# Factorial =========================================================

n = int(input("Enter a non-negative integer: "))

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Factorial:", factorial(n))

# factorial with recurrsion

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))



# Is Prime Number ========================================

n = int(input("Enter a non-negative integer: "))

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(is_prime(n))


# Table in Table Formate  =======================

n = int(input("Enter integer: "))

for i in range(1,11):
    print(f'{n} * {i} = {n*i}')



# Vowel Count =================

st=input("Enter a Word =")
def count_vowel(st):
    return sum(1 for ch in st.lower() if ch in 'aeiou')
print(count_vowel(st))

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


# decorator

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# maximum in list without max()
def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([10, 50, 30]))  

# reverse string

def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("hello"))  

# armstrong

def is_armstrong(n):
    num = n
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    return total == num

print(is_armstrong(153)) 


# question vowel and consonent count ==============

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = c = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1
    return v, c

v, c = count_vowels_consonants("Python")
print("Vowels:", v, "Consonants:", c)  


# question second largest number ============================

def second_largest(nums):
    first = second = float('-inf')
    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    return second

print(second_largest([4, 7, 2, 9, 7])) 
