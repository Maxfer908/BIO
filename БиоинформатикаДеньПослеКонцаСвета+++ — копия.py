def func(read, k):
    mas = []
    for i in range(len(read) - k + 1):
        mas.append(read[i:k + i])
    return mas
def update_g(mas,dict):
    for i in range(0, len(mas) - 1):
        if mas[i] not in dict:
            dict[mas[i]] = {}
        if mas[i + 1] not in dict[mas[i]]:
            dict[mas[i]][mas[i + 1]] = [0,mas[i]+mas[i+1][k:]]
        dict[mas[i]][mas[i + 1]][0] += 1.0
    return dict
def update_reverse_g(mas,dict):
    for i in range(0, len(mas) - 1):
        if mas[i+1] not in dict:
            dict[mas[i+1]] = {}
        if mas[i] not in dict[mas[i+1]]:
            dict[mas[i+1]][mas[i]] = [0,mas[i]+mas[i+1][k-1:]]#]
        dict[mas[i+1]][mas[i]][0] += 1.0
    return dict
def o(file):
    with open(file) as f:
        ref = []
        t = 0
        for line in f:
            if t == 0:
                t += 1
            elif t == 1:
                ref.append(line.strip())
                t += 1
            elif t == 2:
                t += 1
            elif t == 3:
                t = 0
    return ref


def create_g_from_fastq(file,k):
    dict = {}
    dict2={}
    ref = o(file)
    for i in ref:
        mas = func(i, k)
        dict = update_g(mas, dict)
        dict2=update_reverse_g(mas,dict2)
    return dict, dict2
def dump_graph(outgoing, viz_fname):
    with open(viz_fname, 'w') as out_f:
        print('digraph ag{', file=out_f)
        for left, dict in outgoing.items():
            for right in dict:
                round_coverage = dict[right]
                print(left + '[label="{}"]'.format(left), file=out_f)
                print(right + '[label="{}"]'.format(right), file=out_f)
                print(
                    left + ' -> ' + right +
                    '[label="C = {}"]'.format(round_coverage),
                    file=out_f)
        print('}', file=out_f)
def short_cut(out, in_):
    for key in list(out.keys()):
        if key not in in_:
            continue
        if len(out[key]) != 1 or len(in_[key]) != 1:
            continue
        prev=list(in_[key].keys())[0]
        post=list(out[key].keys())[0]
        out[prev][post]=out[key][post]
        in_[post][prev]=in_[key][prev]
        out[prev][post][1]+=prev[k-1:]
        in_[post][prev][1]+=post[k-1:]
        del(out[key])
        del(in_[key])
        del(out[prev][key])
        del(in_[post][key])
    return(out,in_)

    return(out,in_)
file=input()
k = int(input())
g_dict, rev_g_dict=create_g_from_fastq(file,k)
print(g_dict,rev_g_dict)
g_dict,rev_g_dict=short_cut(g_dict,rev_g_dict)
print(g_dict,rev_g_dict)
dump_graph(g_dict,'aut.txt')