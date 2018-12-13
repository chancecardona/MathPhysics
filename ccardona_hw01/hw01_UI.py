import part1 as p1, part2 as p2, part3 as p3

factorialNum = int(input("Enter a number to find its factorial:  "))
print(p1.factorial(factorialNum))
sumNum = int(input("Enter a number to find the sum from 1 to n:  "))
print(p1.sum_nums(sumNum))
stdTime = int(input("Enter a number of seconds to convert to a standard time format:  "))
print(p2.time_conversion(stdTime))
strVowel = input("Enter a string to count the vowels it contains:  ")
print(p2.count_vowels(strVowel))
strPal = input("Enter a string to see if it is a palindrome:  ")
print(p3.palindrome(strPal))
numTwo = int(input("Enter a number to see if it is a power of two:  "))
print(p3.is_power_of_two(numTwo))
