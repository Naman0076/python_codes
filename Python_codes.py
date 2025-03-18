#Basic Calclator
num1 = float(input("Enter first number: "))  
op = input("Enter operator (+, -, *, /): ")  
num2 = float(input("Enter second number: "))  

if op == '+':
    print("Result:", num1 + num2)  
elif op == '-':
    print("Result:", num1 - num2)  
elif op == '*':
    print("Result:", num1 * num2)  
elif op == '/':
    print("Result:", num1 / num2 if num2 != 0 else "Error! Division by zero.")  
else:
    print("Invalid operator!")  

#Palindrome (String):
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

word = input("Enter a string: ").lower()

if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

#Count element occuring once (aabbbaac):
s = input("Enter a string: ")
s = s.lower()
count ={}
for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
unique_char = {}
for char in count:
    if count[char] == 1:
        unique_char [char] = 1
print(count)
print(unique_char)

#Another way using "GET"
s = input("Enter a string: ")
count = {}
for char in s:
    count[char] = count.get[char,0] + 1
for char in count:
    if count[char] == 1:
        print(char)

#Binary Search for Sorted Array:
arr = list(map(int, input("Enter the sorted aray and seperate them by using space: ").split()))
x = int(input("Enter the target Element: "))
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>= x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid +1, high, x)
    else:
        return -1
result = binary_search(arr, 0, len(arr)-1, x)
if result == -1:
    print("element not present !")
else:
    print(f"here is your element : {result}")

#Binary Search using Buble Sort:
arr = list(map(int, input("Enter array and seperate them by using space: ").split()))
x = int(input("Enter the target Element: "))

def bubble_sort(arr):
    n = len(arr)
    for i in range (n-1):
        for j in (n - i - 1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    return arr

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>= x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid +1, high, x)
    else:
        return -1
print(f"sorted array: {arr}")
result = binary_search(arr, 0, len(arr)-1, x)
if result == -1:
    print("element not present !")
else:
    print(f"here is your element : {result}")

def binary_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return -1

#Binary Search Iterative:
arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
x = int(input("Enter the number to search: "))

result = binary_search(arr, x)

if result == -1:
    print("Element not present!")
else:
    print(f"Element found at index {result}")

#Anagrams:
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
def char_count(string):
    char_count ={}
    for char in string.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def anagrams(str1, str2):
    return char_count(str1) == char_count(str2)
if anagrams(str1, str2):
    print("it is an anagram: ")
else:
    print("NO")

#Isograms:
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
def char_count(word):
    count_dict = {}
    for char in word:
        char = char.lower()
        if char in count_dict:
         count_dict[char] +=1
        else:
            count_dict[char] = 1
    return count_dict
char_count_1 = char_count(str1)
char_count_2 = char_count(str2)

values1 = sorted(char_count_1.values())
values2 = sorted(char_count_2.values())

print(f"char count for first: {char_count_1}")
print(f"char count for second: {char_count_2}")

print(f"Sorted frequency values for 1st string: {values1}")
print(f"sorted frequency values for 2nd string: {values2}")

if values1 == values2:
    print("!yes!")
else: 
    print("!NO!")

#sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(abs(num)))

#factorial of a number (iterative):
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial (Iterative):", factorial_iterative(num))

#recursive:
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

num = int(input("Enter a number: "))
print("Factorial (Recursive):", factorial_recursive(num))

#Equilibrium Index:
def find_equilibrium_indices(arr):
    total_sum = sum(arr)
    left_sum = 0
    equilibrium_indices = []

    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            equilibrium_indices.append(i)
        left_sum += num

    return equilibrium_indices

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = find_equilibrium_indices(arr)

if result:
    print("Equilibrium indices:", result)
else:
    print("No equilibrium index found.")


#Group anagrams:
from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)

    for word in words:
        sorted_word = "".join(sorted(word))  # Sort characters to create a unique key
        anagrams[sorted_word].append(word)

    return list(anagrams.values())

words = input("Enter words separated by spaces: ").split()
result = group_anagrams(words)

print("Grouped anagrams:", result)

#first and last index
def left(arr, start, end, x):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid - 1] != x:  
                return mid
            end = mid - 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def right(arr, start, end, x):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            if mid == end or arr[mid + 1] != x: 
                return mid
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1

arr = list(map(int, input("Enter the array using space: ").split()))
x = int(input("Enter a target value: "))
n = len(arr)

l = left(arr, 0, n - 1, x)
r = right(arr, 0, n - 1, x)

if l == -1 or r == -1:
    print("!!! NOT FOUND !!!")
else:
    print(f"Here is your solution: First index = {l}, Last index = {r}")