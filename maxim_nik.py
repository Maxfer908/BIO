def score(a, b):
    if a == b:
        return 1
    else:
        return -1


from pprint import pprint




def align(s, t):
    x = []
    u = []
    for i in range(0, (len(s) + 1)):
        r = []
        q = []
        for j in range(0, (len(t) + 1)):
            r.append(0)
            q.append(0)
        x.append(r)
        u.append(q)

    for i in range(0, len(x)):
        if i == 0:
            for j in range(0, len(x[0])):
                x[0][j] = 0
        else:
            x[i][0] = 0

    m = [0, 0]
    mx = 0

    v = ''
    w = ''

    for i in range(1, len(x)):
        for j in range(1, len(x[0])):
            r = x[i][j - 1] + score('-', t[j - 1])
            k = x[i - 1][j] + score(s[i - 1], '-')
            d = x[i - 1][j - 1] + score(s[i - 1], t[j - 1])

            if r > d and r > k:
                x[i][j] = r
                u[i][j] = '-'
            elif k > r and k > d:
                x[i][j] = k
                u[i][j] = '|'
            else:
                x[i][j] = d
                u[i][j] = 'd'

            if x[i][j] <= 0:
                x[i][j] = 0
                u[i][j] = '.'

            if x[i][j] >= mx:
                m[0] = i
                m[1] = j
                mx = x[i][j]

    for y in range(0, len(u)-1):
        u[y][0] = '.'

    for y in range(0, len(u[0])-1):
        u[0][y] = '.'

    i = m[0]
    j = m[1]

    while (i > 0 or j > 0) and u[i][j] != '.':
        if u[i][j] == '|':
            v = s[i - 1] + v
            w = '-' + w
            i -= 1
        if u[i][j] == "-":
            v = '-' + v
            w = t[j - 1] + w
            j -= 1

        if u[i][j] == "d":
            v = s[i - 1] + v
            w = t[j - 1] + w
            i -= 1
            j -= 1

    return i
with open('aut.txt','w') as out:
    with open('small_ref.fa') as f:
        ref_1=''
        ref_name1=''
        first=True
        for line in f:
            if first:
                first=False
                ref_name1=line.strip()
                continue
            ref_1+=line.strip()
            print(ref_1,ref_name1)

        with open ('small.fastq') as f2:
            ref_name = ''
            ref = ''
            t = 0
            ref_a = ''
            for line in f2:
                if t == 0:
                    ref_name = line.strip()
                    t += 1
                    continue
                if t == 1:
                     ref = line.strip()
                     t += 1
                     continue
                if t == 2:
                     t += 1
                     continue
                if t == 3:
                    ref_a = line.strip()
                    t=0
                i=str(align(ref,ref_1))

                print(ref_name,ref_name1,ref,i,ref_a, file=out, sep='\t')
                continue