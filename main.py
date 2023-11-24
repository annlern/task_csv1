lol={}
with open ('out.csv') as f:
    for line in f:
        line=line.split(',')
        k=line[2]
        for i in range (0, len(k)):
            if k[i]=='@':
                m=k[i+1:]
        if m in lol:
            lol[m] +=1
        else:
            lol[m] =1
sort_lol = sorted(lol.items(), key=lambda x: x[1], reverse=True)
sort_lol2= dict(sort_lol)
kek=open('kek.csv', 'w+')
cheburek='domen, count'+'\n'
kek.write(cheburek)
for i in sort_lol:
    cheburek = str(i[0]) + ', ' + str(i[1])+'\n'
    kek.write(cheburek)
print(kek)

        
