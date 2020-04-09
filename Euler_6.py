
square_sum = 0
add_sum = 0
for i in range(1,101):
    square_sum += i**2
for i in range(1,101):
    add_sum += i
    if i == 100:
        add_sum = add_sum**2

print(add_sum-square_sum)