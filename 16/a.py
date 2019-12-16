d = [int(x) for x in "59762574510031092870627555978901048140761858379740610694074091049186715780458779281173757827279664853239780029412670100985236587608814782710381775353184676765362101185238452198186925468994552552398595814359309282056989047272499461615390684945613327635342384979527937787179298170470398889777345335944061895986118963644324482739546009761011573063020753536341827987918039441655270976866933694280743472164322345885084587955296513566305016045735446107160972309130456411097870723829697443958231034895802811058095753929607703384342912790841710546106752652278155618050157828313372657706962936077252259769356590996872429312866133190813912508915591107648889331"]


#d = [int(x) for x in "03036732577212944063491565474664"]
#d = [int(x) for x in "80871224585914546619083218645595"]

d = d * 10000

# patterns = {}
#
# for s in range(0, len(d)):
#
#     pattern = [0] * (s + 1)
#     pattern += [1] * (s + 1)
#     pattern += [0] * (s + 1)
#     pattern += [-1] * (s + 1)
#
#     fpattern = []
#
#     while len(fpattern) < len(d) + 10:
#         fpattern += pattern
#
#     pattern = fpattern[1:len(d) + 2]
#
#     patterns[s] = pattern
#
#     print(s)

# from multiprocessing.pool import ThreadPool
#
#
# def do(a):
#
#     s2, lll2, d2 = a
#
#     t = 0
#
#     c_pos = 0
#
#     c_pos = s2
#
#     while c_pos < lll2:
#
#         t += sum(d2[c_pos:min(c_pos + s2 + 1, lll2)])
#         c_pos = c_pos + s2 * 2 + 2
#         t -= sum(d2[c_pos:min(c_pos + s2 + 1, lll2)])
#         c_pos = c_pos + (s2 + 1) * 2
#
#     if t < 0:
#         t = -t
#
#     return t % 10
#
# for p in range(0, 100):
#
#     new_l = []
#
#     lll = len(d)
#
#
#     print(p)
#     new_l = ThreadPool(5).map(do, [(x, lll, d) for x in range(0, lll)])
#
#     d = new_l
#
#     print(p)
#
# print(new_l)
#
#
#


offset = 5976257
#offset = 303673


c_pos = offset

for _ in range(0, 100):

    full_sum = sum(d[offset:])

    for x in range(offset, len(d)):
        t = full_sum
        full_sum = full_sum - d[x]
        if t < 0:
            t = -1

        d[x] = t % 10

    print(_)

print(d[offset:offset+8])
