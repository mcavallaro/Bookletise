import sys

__version__ = '0.1'

def doppioAnagniPanoramic(number):
    '''
    Build the index vector, con doppio Anagni "panoramic"
    '''
    index1 = range(1, int(number / 2 + 1))
    index2 = range(number, int(number / 2), -1)
    index = []
    i = 0
    index.append(index2[0])
    while True:
        # rearrange, con DOPPIO ANAGNI
        index.append(index1[i])
        index.append(index1[i+1])
        i = i + 1
        index.append(index2[i])
        i = i + 1
        if i >= (number / 2):
            break
        index.append(index2[i])
    return index


def doppioAnagniCrazy(number, pages, max_tmp):
    '''
    Build the index vector, con doppio Anagni "crazy"
    '''
    index1 = range(1 + max_tmp, int(number / 2 + 1 + max_tmp))
    index2 = ['NA' for _ in range(number - pages)] + list(range(pages + max_tmp, int(number / 2 + max_tmp), -1))
    index = []
    i = 0
    index.append(index2[0])
    while True:
        # rearrange, con DOPPIO ANAGNI
        index.append(index1[i])
        index.append(index1[i+1])
        i = i + 1
        index.append(index2[i])
        i = i + 1
        if i >= int(number / 2):
            break
        index.append(index2[i])
    return index


def bookletise(n_pages_booklet, total_pages):
    '''
    Print the ordered page numbers, to make booklets of `n_pages_booklet' pages,
    out of a total of 'total_pages' pages.
    '''

    if (n_pages_booklet % 4):
        sys.stderr.write('Each booklet block must contain multiple-of-four number of pages.')
        return

    lista_in = doppioAnagniPanoramic(n_pages_booklet)
    lista = lista_in[:]

    i=0
    while True:
        i = i + 1
        lista_tmp = [p + n_pages_booklet*i for p in lista_in]
        lista = lista + lista_tmp
        if lista[n_pages_booklet*i] + n_pages_booklet > total_pages:
            break

    sys.stdout.write(str(lista[0]))
    for l in lista[1:]:
        sys.stdout.write(",%d" % l)

    max_tmp = lista[n_pages_booklet*i]

    pages_left = total_pages - max_tmp

    if pages_left:

        sys.stdout.write("\nThere are %d pages left,\n" % pages_left)

        last_group = int(pages_left/4)*4 + 4*bool(pages_left%4)

        sys.stdout.write(" make another booklet of %d pages\n" % last_group)

        last_booklet = doppioAnagniCrazy(last_group, pages_left, max_tmp)

        sys.stdout.write(str(last_booklet[0]))
        for l in last_booklet[1:]:
            sys.stdout.write(',' + str(l))

    sys.stdout.write('\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('Usage: python bookletise.py n_pages_booklet total_pages')
    bookletise(int(sys.argv[1]), int(sys.argv[2]))
