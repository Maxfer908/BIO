from pprint import pprint
import math
results=[]
people=[]
q=[0,0]
first=True
with open('norm_camp.tsv') as f:
    for line in f:
        mid_con=0
        mid_cas=0
        info = line.strip().split('\t')
        if first==True:
            for i in range(0,len(info)):
                if info[i]=='control':
                    people.append(1)
                    q[0]+=1
                elif info[i]=='case':
                    people.append(2)
                    q[1]+=1
                else:
                    people.append(0)
                    i+=1
            first=False
            print(people)
        else:
            con=0
            case=0
            for i in range(0,len(info)-1):
                if i==0:
                    i+=1
                elif people[i]==1:
                    con+=float(info[i])
                    i+=1
                elif people[i]==2:
                    case+=float(info[i])
                    i+=1
            results.append([info[0],float(con/q[0]),float(case/q[1])])
pprint(results)
with open('aut.txt','w') as out:
    for i in range(0,len(results)):
         log=math.log2(results[i][2]/results[i][1])
         if log>=0.1 or log<=-0.1:
             print(results[i][0],log,file=out,sep='\t')