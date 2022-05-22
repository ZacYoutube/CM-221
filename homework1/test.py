from itertools import product
def possible_kmers():
  return [''.join(x) for x in product('ATGC', repeat=4)]

q = 0
for k in possible_kmers():
    q = q + 1
    print(k,q)