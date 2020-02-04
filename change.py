def getInput():
    try:
        infile = open('data.txt', 'r')
    except IOError:
        print("File IO Error")
        quit()
    finally:
        return infile.readlines()

def putOutput(arr):
    try:
        outfile = open('change.txt', 'w')
    except IOError:
        print("File IO Error")
        quit()
    finally:
        for k in arr:
            outfile.write("%s " % k)
            outfile.write('\n')
        return

def change(c, k, n):
    tn = n
    tk = k
    result = []
    while tn != 0:
        if c**k <= tn:
            result.append(c**k)
            tn -= c**k
        else:
            k -= 1

    return result

def main():

    ins = list(map(str.strip, getInput()))

    results = []

    for v in ins:
        args = v.split()
        results.append(change(int(args[0]), int(args[1]), int(args[2]) ))

    final = []
    ctr = 0

    for r in results:
        ctr += 1
        final.append(str("Optimal Set " + str(ctr)))
        while r != []:
            final.append( [r[0], r.count(r[0])] )
            r = list(filter(lambda a: a != r[0], r))

    putOutput(final)

    return 0

main()
