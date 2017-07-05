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


s="AAAAAAAAAAA"
t='AGCAAAAC'
x=[]
u=[]
align(s,t)
for i in range(0,len(x)):
    if i==0:
        for j in range(0,len(x[0])):
            x[0][j]=j*(-1)

    else :
        x[i][0]=i*(-1)

pprint(x)
for i in range(1,len(x)):
    for j in range(1,len(x[0])):
        print(i,' ',j)
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
pprint(u)
pprint(x)
i=len(u)-1
print(i)
j=len(u[0])-1
print(j)
v=''
w=''
for y in range(1,len(u)-1):
    u[y][0]='|'
for y in range(1,len(u[0])-1):
    u[0][y]='-'
pprint(u)
pprint(x)
while i!=0 or j!=0:
    print(i,j)
    if u[i][j]=="d":
        v = s[i-1]+v
        w=t[j-1]+w
        i-=1
        j-=1
    if u[i][j]=='|':
        w='-'+w
        v=s[i-1]+v
        i-=1
    if u[i][j]=="-":
        v='-'+v
        w=t[j-1]+w
        j-=1
pprint(x)
pprint(u)
print(w)
print(v)


