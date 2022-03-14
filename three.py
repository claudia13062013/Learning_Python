list=[]
for i in range(1,11):
    list.append((i+111)/2) 
for i in list:
    if i%2==0:
        list.remove(i)
print("To jest lista bez liczb parzystych :")
print(list)
