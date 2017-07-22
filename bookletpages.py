import sys

def doppioanagnipanoramic(number):
    ''' Build the index vector con doppio Anagni "panoramic" '''
    index1 = range(1, number / 2 + 1)
    index2 = range(number, number / 2, -1)
    index = []
    i = 0
    index.append(index2[0])
    while True:
        # rearrange con DOPPIO ANAGNI
        index.append(index1[i])
        index.append(index1[i+1])
        i = i + 1
        index.append(index2[i])
        i = i + 1
        if i >= (number / 2):
            break
        index.append(index2[i])
    return index


def doppioanagnicrazy(number, pages, max_tmp):
    ''' Build the index vector con doppio Anagni "crazy" '''
    index1 = range(1 + max_tmp, number / 2 + 1 + max_tmp)
    index2 = ['NA' for _ in xrange(number - pages)] + range(pages + max_tmp, number / 2 + max_tmp, -1)
    index = []
    i = 0
    index.append(index2[0])
    while True:
        # rearrange con DOPPIO ANAGNI
        index.append(index1[i])
        index.append(index1[i+1])
        i = i + 1
        index.append(index2[i])
        i = i + 1
        if i >= (number / 2):
            break
        index.append(index2[i])
    return index


pages_booklet = int(sys.argv[1])
total_pages = int(sys.argv[2])

lista_in = doppioanagnipanoramic(pages_booklet)
lista = lista_in[:]

i=0
while True:
    i = i + 1
    lista_tmp = [p + pages_booklet*i for p in lista_in]
    lista = lista + lista_tmp
    if lista[pages_booklet*i] + pages_booklet > total_pages:
        break

for l in lista:
#    print 
    sys.stdout.write("%d," % l)
#    sys.stdout.write(', ')

max_tmp = lista[pages_booklet*i]

pages_left = total_pages - max_tmp

sys.stdout.write("\nThere are %d pages left," % pages_left)

last_group = (pages_left/4)*4 + 4*bool(pages_left%4)

sys.stdout.write(" make another booklet of %d pages\n" % last_group)

last_booklet = doppioanagnicrazy(last_group, pages_left, max_tmp)

for l in last_booklet:
    sys.stdout.write(str(l) + ',')

