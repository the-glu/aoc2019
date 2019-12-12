data = """<x=17, y=-9, z=4>
<x=2, y=2, z=-13>
<x=-1, y=5, z=-1>
<x=4, y=7, z=-7>"""

moons = []

for i in data.split('\n'):

    i2 = i.split(',')

    print(i2)

    x = i2[0][3:]
    y = i2[1][3:]
    z = i2[2][3:-1]

    moons.append({
        'p': {
            'x': float(x),
            'y': float(y),
            'z': float(z),
        }, 'v': {
            'x': 0.0,
            'y': 0.0,
            'z': 0.0,
        },
        'i': {
            'x': float(x),
            'y': float(y),
            'z': float(z),
        },
    })


c = 0

pe = 0

vls = []


for x in range(0, 1000000):

    for m in moons:
        for m2 in moons:
            for a in ['x', 'y', 'z']:
                if m['p'][a] < m2['p'][a]:
                    m['v'][a] += 1
                if m['p'][a] > m2['p'][a]:
                    m['v'][a] -= 1

    for m in moons:
        for a in ['x', 'y', 'z']:
            m['p'][a] += m['v'][a]


    ok = True
    for m in moons:
        for a in ['z']:
            if m['v'][a] != 0 or m['i'][a] != m['p'][a]:
                ok = False
                break

    c += 1

    if ok:
        break


# 231614 96236

print(c)

#
#
# e = 0
#
# for m in moons:
#     p = abs(m['p']['x']) +abs(m['p']['y']) +abs(m['p']['z'])
#     k = abs(m['v']['x']) +abs(m['v']['y']) +abs(m['v']['z'])
#
#     e+= p*k
#
#
# print(e)
