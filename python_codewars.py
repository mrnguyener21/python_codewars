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
def positive_sum(arr):
    sum = 0
    for x in arr:
        if x > 0:
            sum = sum +x
    return sum
print(positive_sum([1,2,3]))