#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

biggest = []
for first_number in range(100,999):
    for second_number in range(100,999):
        num = str(second_number*first_number)
        if num == num[::-1]:
            biggest.append(second_number * first_number)
print(max(biggest))

