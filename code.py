def function1(sequence): # setup fucntion
    nuc_counts = dict() # intilize a dict var
    for nucleotide in sequence:
        if nucleotide not in nuc_counts: 
            nuc_counts[nucleotide] = 1 # setup count of 1 if nuc is not in dict var 
        else:
            nuc_counts[nucleotide] += 1 # for every other occurence of nuc update 1 the dict var
    return nuc_counts # return updated dict var

def function2(a): 
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))


def function1(a):
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))

