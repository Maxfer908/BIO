def count(sam,u):
    with open(sam) as sam:#открытие первого sam-а
        i = 0
        j = 0
        for line in sam:
            if line[0] == '@':
                continue
            rid_info = line.strip().split('\t')
            beg = int(rid_info[3])
            end = beg+len(rid_info[9])
            flag = int(rid_info[1])
            if flag & 16:
                flag='-'
            else:
                flag='+'
            if flag=='+':
                while i<len(g_mas):
                    if end<g_mas[i][1]:
                        break
                    elif beg>g_mas[i][2]:
                        i+=1
                    else:
                        g_mas[i][u]+=1
                        break

            if flag=='-':
                while j<len(g_mass):
                    if end<g_mass[j][1]:
                        break
                    elif beg>g_mass[j][2]:
                        j+=1
                    else:
                        g_mass[j][u]+=1
                        break

file='genome_annotation.gtf'
SAM='THYP2_22.sam'
SAM1='TNOR2_22.sam'
i=0
j=0
g_mas=[]#массив для данных генов
g_mass=[]
with open(file) as f:
    for line in f:

        gene_info=line.strip().split('\t')
        t=str(gene_info[8])
        t=t.strip().split(';')
        t1=t[2]
        t1=t1.strip().split('"')
        g_name=t1[1]
        x1=int(gene_info[3])#начало гена
        x2=int(gene_info[4])#конец гена
        side=gene_info[6]# + или -
        if side=='+':
            g_mas.append([g_name,x1,x2,side,0,0])
        else:
            g_mass.append([g_name,x1,x2,side,0,0])

count(SAM,4)
count(SAM1,5)

i=0
j=0
with open('aut.txt','w') as out:
        for gene in g_mas:
            print(gene[0], gene[4], gene[5], file=out, sep='\t')
        for gene in g_mass:
            print(gene[0], gene[4], gene[5], file=out,sep='\t')




