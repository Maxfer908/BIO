def func(mas):
    result=0
    p=0
    for i in range(0,len(mas)-1):
        if mas[i]==mas[i+1]:
            p+=1
            print(p,mas[i],mas[i+1],i)
        else:
            if p>=result:
                result=p+1
                p=0

    return result
mas=[3,3,3,3,2,2,2,2,2,2,2,2,2,0]
print(func(mas))

