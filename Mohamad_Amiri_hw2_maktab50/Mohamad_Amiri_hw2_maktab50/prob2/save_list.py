n=int(input("enter number of your data"))

save_list=[]


for i in range(n):
    save_list.append(input("Enter your numbers"))

print(save_list)

save_tpl=tuple(save_list)
print(save_tpl)
