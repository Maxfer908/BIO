from pprint import pprint
def swap_columns(a,i,j):
    for x in range(0,len(a)):
        h=a[x][i]
        a[x][i]=a[x][j]
        a[x][j]=h
    return a



i=int(input())
j=int(input())
a=[[1,2,3,4,5,6],[1,9,4,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
pprint(swap_columns(a,i,j))