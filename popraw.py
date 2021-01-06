import random
f1 = open('nazwiska.txt', encoding="utf8")
f2 = open('miasta.txt','w')
tab1 = []
tab = []
for x in f1:
    tab1.append(x.split())
for x in range(len(tab1)):
    if not(not x):
        print(x)
        for y in range(len(tab1[x])):
            if y==1:
                print(tab1[x][y])
                f2.write((str(tab1[x][y]).replace("'",'').replace('[','').replace(',','').replace(']','')+"\n"))
f1.close()
f2.close()
tab = [1,2,3]
x = random.randint(0,1)
if x:
    print(x)
f1 = open("uczelnie.txt","r")
tab = []
for x in f1:
    tab.append(x)
    tab.append("")
print(type(tab))


