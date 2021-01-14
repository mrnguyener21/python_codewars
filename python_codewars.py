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
