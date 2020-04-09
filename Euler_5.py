
j = 1000
i = 1
my_list = []
while i <= 20:
    if j % i == 0:
        i += 1
    else:
       j += 10
       i = 1
    my_list.append(j)
print(max(set(my_list)))

