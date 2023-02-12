mylist = [1,2,3,4,5,6,7,8,9,10]
even_list=[]
for x in mylist:
    if x % 2 == 0:
        even_list.append(x)
print(even_list)
i = 0
while i < len(mylist):
    if mylist[i] % 2 == 0:
        even_list.append(mylist[i])
    i += 1
print(even_list)
