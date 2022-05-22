from itertools import product
filename = 'rosalind_kmer.txt'
text_file = open(filename, "r")
data = text_file.read().split("\n",1)[1]
data = data.replace('\n', '')
text_file.close()

def getAllKmers():
    arr = []
    arr = [''.join(x) for x in product('ATCG', repeat=4)]
    return arr

def kmerCompositionCounts(k, data):
    kmer_map = {}
    kmer_ctn = []

    for permutation in getAllKmers():
        kmer_map[permutation] = 0
    
    for i in range(len(data)+1-k):
        kmer = data[i:i+k]
        kmer_map[kmer] += 1
    
    sorted_kmers = sortArrLexicographically(kmer_map.keys())

    for kmer in sorted_kmers:
        kmer_ctn.append(kmer_map[kmer])
    
    return kmer_ctn
        
def sortArrLexicographically(arr):
    return sorted(arr); 

def formatArrayOutput(arr):
    print(' '.join(map(str, arr)))



formatArrayOutput(list(kmerCompositionCounts(4, data)))




