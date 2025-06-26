name1=input("Enter name one:")
name2=input("Enter name two:")
list1=list(name1)
list2=list(name2)
c=0
def count():
    global list1
    global list2
    for i in list1:
        for j in list2:
            if j==i:
                list1.remove(i)
                list2.remove(j)
                count()
count()
c=len(list1)+len(list2)
flames=list("flames")
temp=[]
b=1
while 1:
    if len(temp)==5:
        break
    for i in flames:
        if i not in temp:
            if b==c:
                b=0
                temp.append(i)
            b+=1
for i in flames:
    if i not in temp : print(i)