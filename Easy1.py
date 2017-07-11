def func(n):
    result=0
    while n>0:
        result+=n*(n-1)
        n-=1
        print(result)
    return result

n=int(input())
print(func(n))