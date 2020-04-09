#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
i = 8
j = 2
prime_list = [2,3,5,7]
print(sum(prime_list))
while max(prime_list) < 2000000:
    if i % j == 0 and i == j:
        prime_list.append(i)
        i += 1
        j = 2
    elif i % j == 0 and i != j:
         i += 1
         j = 2
    else:
        j += 1

print(sum(prime_list))