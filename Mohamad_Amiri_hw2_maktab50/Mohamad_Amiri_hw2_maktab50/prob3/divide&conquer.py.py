#divide&conquer

my_value=[12, -1, 32, 41, 64, 5, 1236, 0, 3, 9, 6]

left_value=my_value[0:5]
right_value=my_value[5:]

print("first partition:",left_value)
print("second partition",right_value)

minimum_left=maximum_left=left_value[0]
minimum_right=maximum_right=right_value[0]

for i in range(5):
    if left_value[i]< minimum_left:
        minimum_left=left_value[i]

    elif left_value[i]>maximum_left:
        maximum_left=left_value[i]
        
for i in range(5):
    if right_value[i]< minimum_right:
        minimum_right=right_value[i]

    elif right_value[i]>maximum_right:
        maximum_right=right_value[i]
        
if maximum_right>maximum_left:
    print("maximum:",maximum_right)
else:
    print("maximum:",maximum_left)

if minimum_left<minimum_right:
    print("minimum:",minimum_left)

else:

    print("minimum:",minimum_right)
print("summation:",sum(my_value))