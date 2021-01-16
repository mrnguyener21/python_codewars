# EVEN OR ODD
#Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
# def even_or_odd(number):
#     if number%2 == 0:
#         return'Even'
#     else:
#         return 'Odd'



# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.
# def positive_sum(arr):
#     sum = 0
#     for x in arr:
#         if x > 0:
#             sum = sum +x
#     return sum
# print(positive_sum([1,2,3]))


#opposite number
# Very simple, given a number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34\
# def opposite(number):
#     return number * -1

# print( opposite(26.5))


#sum of positive
# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.
# def postive_sum(arr):
#     sum = 0;
#     for x in arr:
#         if x > 0:
#             sum = sum + x;
#     return sum;

# print(postive_sum([1,2,3,4,5]))

#Opposite Number
#given a number, find it's positive
# def oppositve(number):
#     return number * -1


# Your goal is to create a function that removes the first and last characters of a string. 
# You're given one parameter, the original string. 
# You don't have to worry with strings with less than two characters.
# def remove_char(s):
    #split the string up and then pop, lock and concatonate 
    # x = list(s)
    # x.pop(0)
    # x.pop(len(x)-1)
    # return ''.join(x)

    #below is the best way to go about it using slice notion
# def remove_char(s):
#     return s[1:-1]

# print(remove_char('too'))


#return negative
#return the given number negative. If it is already negative than just turn it
# def make_negative( number ):
#     if number > 0:
#         return number * -1;
#     else:
#         return number;


#string repeat
# Write a function called repeat_str which repeats the given string src exactly count times.

# repeatStr(6, "I") // "IIIIII"
# repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

# def repeat_str(repeat, string):
    #below was my solution
    # x= []
    # r = repeat
    # while r > 0:
    #     # print(r)
    #     x.append(string)
    #     r =r - 1
    # return ''.join(x)
# repeat_str(2,'hello')
    #below is best practice
#     return repeat * string
# print(repeat_str(2,'hello'))   
# print('hello')


#Remove String Spaces
#remove the spaces from the string, then return the resultant string
# def no_space(x):
    #below is my code
    # split = list(x);
    # y = [];

    # for character in split:
    #     if character != ' ':
    #         y.append(character);
            
    # return ''.join(y);

    #below is best practice
    # return x.replace(' ','')
# no_space('a b c ')
# print(no_space('a b c '))

#reversed sstrings
#complete the solution so that it reverses the  string passed into it
# def solution(string):
    #below is my code
    # x = list(string)
    # y = len(x)
    # z = [];
    # while y > 0:
    #     z.append(x[y - 1])
    #     y = y-1
    # return ''.join(z)

    #below is best practice
    # return string[::-1]

# print(solution('world'))



#find the smallest integer
# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

# def find_smallest_int(arr):

    #below is my code
    # x = sorted(arr)
    # return x[0]

    #below is best practice
    # return min(arr)


# find_smallest_int([78, 56, 232, 12, 11, 43])
# print(find_smallest_int([78, 56, 232, 12, 11, -43]))


#Convert boolean values to strings 'Yes' or 'No'.
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
# def bool_to_word(boolean):
#     if boolean == True:
#         return 'Yes';
#     elif boolean == False:
#         return 'No';



#vowel count
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

# def get_coun(input_str):
    # below is my code
    # x = list(input_str)
    # z = []
    # for y in x:
        # if y == 'a' or y =='e' or y== 'i'or y== 'u' or y== 'o':
            # z.append(y)
    # return len(z);

    # below is best practice
    # return sum(1 for let in input_str if let in "aeiouAEIOU")
# print(get_coun('abracadabra'))

#mumbling
# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
#first letter repeats once, second letter repeats twice, third letter repeats 3x's etc
#first lettter of the iteration has to be capital, so A-Bb-Ccc-Ddd

# def accum(s):
    # return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
# accum('abcd')
# print(accum('abcd'))