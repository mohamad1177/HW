#defauult solution
my_value=[12, -1, 32, 41, 64, 5, 1236, 0, 3, 9, 6]

minimum=maximum=my_value[0]

for i in range(10):
    if my_value[i]>maximum:
        maximum=my_value[i]

    elif my_value[i]<minimum:
        minimum=my_value[i]

print("minimum:", minimum,"===========","maximum:",maximum)
print("summation:",sum(my_value))
