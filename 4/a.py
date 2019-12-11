r = range(146810, 612564)

v = 0

for x in r:
    p = None
    i = True
    d = False
    d2 = False
    d3 = None

    for y in str(x):

        if p:
            if int(y) < int(p):
                i = False
                break

            if d2:
                if y != p:
                    d = True
                else:
                    d3 = y

                d2 = False

            else:
                if y == p and y != d3:
                    d2 = True

        p = y

    if i and (d or d2):
        print(x)
        v += 1

print(v)
