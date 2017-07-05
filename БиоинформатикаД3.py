def align(s,t):
    for i in range(0,(len(s)+1)):
        r=[]
        q=[]
        for j in range(0,(len(t)+1)):
            r.append(0)
            q.append(0)
        x.append(r)
        u.append(q)
    return x
def score(a,b):
    if a==b:
        return 1
    else:
        return -1

from pprint import pprint


s="CGATCGCATC"
t='CTCCGTAGTG'
x=[]
u=[]
m=[0,0,0,0]
o=0
align(s,t)
for i in range(0,len(x)):
    if i==0:
        for j in range(0,len(x[0])):
            x[0][j]=j*(-1)

    else :
        x[i][0]=i*(-1)

for i in range(1,len(x)):
    for j in range(1,len(x[0])):
        #print(i,' ',j)
        r=x[i][j-1]+score('-',t[j-1])
        k=x[i-1][j]+score(s[i-1],'-')
        d=x[i-1][j-1]+score(s[i-1],t[j-1])
        if r>d and r>k:
            x[i][j]=x[i][j-1]+score(s[i-1],t[j-1])
            u[i][j]='-'
        elif k>r and k>d :
            x[i][j]=x[i-1][j]+score(s[i-1],t[j-1])
            u[i][j]='|'
        else:
            x[i][j]=x[i-1][j-1]+score(s[i-1],t[j-1])
            u[i][j]='d'
        if x[i][j] >=o:
            m[0]=i
            m[1]=j
            o=x[i][j]

print(m)
i=m[0]
j=m[1]
sc=0
while x[i][j]>0:
    r = x[i][j - 1] + score('-', t[j - 1])
    k = x[i - 1][j] + score(s[i - 1], '-')
    d = x[i - 1][j - 1] + score(s[i - 1], t[j - 1])
    if r > d and r > k:
        x[i][j] = x[i][j - 1] + score(s[i - 1], t[j - 1])
        u[i][j] = '-'
        j-=1
    elif k > r and k > d:
        x[i][j] = x[i - 1][j] + score(s[i - 1], t[j - 1])
        u[i][j] = '|'
        i-=1
    else:
        x[i][j] = x[i - 1][j - 1] + score(s[i - 1], t[j - 1])
        u[i][j] = 'd'
        i-=1
        j-=1
    m[2]=i
    m[3]=j
    print('||')
    print(m)
i=len(u)-1
#print(i)
j=len(u[0])-1
#print(j)
v=''
w=''
for y in range(1,len(u)-1):
    u[y][0]='|'
for y in range(1,len(u[0])-1):
    u[0][y]='-'
pprint(u)
pprint(x)
i=m[0]
j=m[1]
while (i>m[2] or j>m[3]) and (i>0 or j>0):
    print(i,j)
    print('SSSSSSS')
    if x[i][j]>0:
        if u[i][j]=='|':
            if x[i][j]>x[i-1][j]:
                print('2')
                w='-'+w
                v=s[i-1]+v
                i-=1
                sc+=1
                print(i, j)
            elif x[i][j]<x[i-1][j]:
                print('2')
                w = '-' + w
                v = s[i - 1] + v
                i -= 1
                sc-=1
                w = '-' + w
                v = s[i - 1] + v
                print(i,j)
        if u[i][j]=="-":
            if x[i][j]>x[i][j-1]:
                print('3')
                v='-'+v
                w=t[j-1]+w
                j-=1
                sc+=1
                print(i, j)
            elif x[i][j-1]>x[i][j]:
                print('3')
                v = '-' + v
                w = t[j - 1] + w
                j -= 1
                sc-=1

        if u[i][j]=="d":
            if x[i][j]>x[i-1][j-1]:
                    print('1')
                    v = s[i-1]+v
                    w=t[j-1]+w
                    i-=1
                    j-=1
                    sc+=1
                    print(i,j)
            else:
                print('1')
                v = s[i - 1] + v
                w = t[j - 1] + w
                i -= 1
                j -= 1
                sc -= 1
    if x[i][j]==0:
        i-=1
        j-=1
if i==0 and j==0:
    sc+=1


print(sc)
print(w)
print(v)