list=[0,1,1]
i=int(input())
b=int(input())
n=2
if i==0:
    print(list[0])
elif i==1:
    print(list[1])
else:
    while(i > 0):
        if b>n:
            list.append(list[n]+list[n-1])
            i-=1
            n+=1
            print(list)
        if n==b:
            list.append(list[n]+list[n-1]-list[n-b+1])
            n+=1
            i-=1
            print(list)
            print(n,' ', b)
        if n>b:
            list.append(list[n] + list[n - 1] - list[n - b])
            n += 1
            i -= 1
            print(list)
            print(n,' ',b)
    print(list[n-2])