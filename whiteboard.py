# Takes a string and returns new string without first and last letter
def trimmer(string):
    return string[1:-1]

print(trimmer("poop"))

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# [1,1,3] ==> 3
# [2,2,2,4,2] ==> 4
def diff(list):
    val = None
    if list[1] == list[0] or list[1] == list[2]:
        for i in list:
            if i != list[1]:
                val = i
                break
    else:
        val = list[1]
    return val


print(diff([1,1,1,1,1,3,1,1,1]))

# Complete the method that takes a boolean value 
# and return a "Yes" string for true, or a "No" string for false.
def string_returner(bool):
    return "yes" if bool else "no"
# Edge case
print(string_returner(None))   

# Create a function that takes 2 numbers in form of a string as an input,
#  and outputs the sum (also as a string) 
def add_strings(a, b):
    return str(int(a) + int(b))

print(add_strings("1", "2"))

# Given a list of words, determine if any of them are palindromes  
# more descriptive  
# def return_palindrome(list):
#     pal_list = []
#     for word in list:
#         if word == word[::-1]:
#             pal_list.append(word)
#     return pal_list
def return_palindrome(list):
    return [word for word in list if word == word[::-1]]

print(return_palindrome(["poop", "hannah", "dog", "cat"]))    

# Write code that outputs the Fibonacci series
def fibonacci():
    fib = [0,1]
    for i in range(1,20):
        fib.append(fib[i] + fib[i-1])
    return fib[1:]

print(fibonacci())    

# Implement FizzBuzz
def FizzBuzz():
    for fizzbuzz in range(20):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
    print(fizzbuzz)

print(FizzBuzz())    