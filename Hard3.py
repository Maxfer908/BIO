from pprint import pprint
def swap_columns(a,i,j):
    for x in range(0,len(a)):
        for y in range(0,len(a[x])):
            if y==i and y+1==j:
                h=a[x][i]
                a[x][i]=a[x][y+1]
                a[x][y+1]=h
    return(a)




a=[[1,2,3,4,5,6],[1,9,4,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
pprint(swap_columns(a,1,2))