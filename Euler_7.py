#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

prime_list = [2,3,5,7]
j = 2
i = 8
print("Wait for it......")
while len(prime_list) != 10001:
    if i % j == 0 and i == j:
        prime_list.append(i)
        i += 1
        j = 2
    elif i % j == 0 and i != j:
         i += 1
         j = 2
    else:
        j += 1


print(max(prime_list))