# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# Input Format

# Read , the year to test.

# Constraints


# Output Format

# The function must return a Boolean value (True/False). Output is handled by the provided code stub.

# Sample Input 0

# 1990
# Sample Output 0

# False
# Explanation 0

# 1990 is not a multiple of 4 hence it's not a leap year.

# def is_leap(year):
#     leap = False
    
#     if year%4 == 0:
#         if year%100 != 0:
#             leap = True
#         else:
#             if year%400 == 0:
#                 leap = True

#     # Write your logic here
    
#     return leap

# print(is_leap(1990))

# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:


# Note that "" represents the consecutive values in between.

# Example

# Print the string .

# Input Format

# The first line contains an integer .

# Constraints


# Output Format

# Print the list of integers from  through  as a string, without spaces.

# Sample Input 0

# 3
# Sample Output 0

# 123


# THE MINION GAME
# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#THERE ARE NO DUPLICATES SO we only add the substring to the array if that substring is not already in the array

# def minion_game(string):
#     # your code goes here
#     x = string
#     kevin = 0
#     stuart = 0
#     vowels = ['A', 'E', 'I', 'O', 'U']

#     for i , j in enumerate(x):
#         if j in vowels:
#             stuart += len(x)-i
#         else:
#             kevin += len(x)-i
            
#     if kevin == stuart:
#         print('Draw')
#     elif kevin > stuart:
#         print('Kevin {}'.format(kevin))
#     else:
#         print('Stuart {}'.format(stuart))


# minion_game('BANANA')
# print(minion_game('BANANA'))


# given an integer, n, perform the following conditional actions:
#     if n is odd, print 'Weird'
#     if n is even and in the inclusive range of 2 to 5, print 'Not Weird'
#     if n is even and in the inclusive range of 6 to 20, print 'Weird'
#     if n is even and greater than 20, print ' not weird'

    # if n%2 != 0:
    #     print('Weird')
    # else:
    #     if n >= 2 and n <= 5:
    #         print('Not Weird')
    #     elif n >= 6 and n <= 20:
    #         print('Weird')
    #     elif n >20:
    #         print('Not Weird')


#The Minion Game
# def minion_game(string):
#     Kevin = 0;
#     Stuart = 0;
#     x = string;
#     vowels = ['A','E','I','O','U']

#     for i, j in enumerate(x): 
#         if j in vowels:
#             Kevin += (len(x) - i);
#         else:
#             Stuart += (len(x) - i)
#     if  Kevin > Stuart:

#         print('Kevin {}'.format(Kevin));
#     elif Stuart > Kevin:
#         print('Stuart {}'.format(Stuart))
#     else:
#         print('Draw') 
# minion_game('BANANA')


#PYTHON: DIVISION
# from __future__ import division

# if __name__ == '__main__':
#     a = int(raw_input())
#     b = int(raw_input())
#     print(a//b);
#     print(a/b);

#ARITHMETIC OPERATORS
#The provided code stub reads two integers from STDIN, a and b. add code to print three lines where:
#1) the first contains the sum of the two numbers 
#2) the second line contains the difference of the two number
#3)the third line contains the product of the two numbers

# print(a+b)
# print(a-b)
# print(a*b)


#LOOPS
#the provided code stub reads and integer, n, from STDIN. for all non-negative integers i<n print i^2
# if __name__ == '__main__':
#     n = int(raw_input())
#     i = 0;
#     for i in range(0,n):
#         print(i*i)

#RE.SPLIT()
#you are given a string 's' consisting only of digits 0-9, commas, and dots.
#your ask is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in s.
#it's guaranteed that every comma and every dot in s is preceeeded and followed by a digit.



#FIND THE RUNNER - UP SCORE!
#Given the paricipants' score sheet for your university sports day, you are required to find the runner up score. you are given n scores. store them in a list and find the score of the runner up.

# if __name__ == '__main__':
#     n = int(raw_input())
#     arr = map(int, raw_input().split())
#     x = list(arr)
#     y = sorted(set(x))
#     print(y[len(y)-2])

