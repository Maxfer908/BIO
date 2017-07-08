def consensus(string):
    gl=['a','e','y','u','i','o']
    for i in range(0,len(string)-1):
        p=0
        if string[i] in gl:
           if string[i+p] not in gl:
                string[i]=string[i+p]
           else:
               p+=1
        if i not in gl:
            if i+p in gl:
                i=i+p
            else:
                p+=1
    print(string)



string='abcdefgh'
print(consensus(string))