import copy


class IC():

    def __init__(self, states_):

        self.states = {}

        for p, v in enumerate(states_):
            self.states[p] = v

        def iF():
            return input("?")

        self.set_in(iF)

        def oF(v):
            print(v)

        self.set_out(oF)

    def set_in(self, iF):
        self.iF = iF

    def set_out(self, oF):
        self.oF = oF

    def run(self):

        states = copy.deepcopy(self.states)

        pos = 0
        rbase = 0

        while True:

            opscode = states[pos] % 100

            tmode = "00000{}".format(states[pos])

            try:
                if tmode[-3] == '0':
                    param1 = states[states[pos + 1]]
                elif tmode[-3] == '1':
                    param1 = states[pos + 1]
                elif tmode[-3] == '2':
                    param1 = states[states[pos + 1] + rbase]
            except KeyError:
                param1 = 0

            try:
                if tmode[-4] == '0':
                    param2 = states[states[pos + 2]]
                elif tmode[-4] == '1':
                    param2 = states[pos + 2]
                elif tmode[-4] == '2':
                    param2 = states[states[pos + 2] + rbase]
            except KeyError:
                param2 = 0

            try:
                if tmode[-5] == '0':
                    dest = states[pos + 3]
                elif tmode[-5] == '1':
                    dest = pos + 3
                elif tmode[-5] == '2':
                    dest = states[pos + 3] + rbase
            except KeyError:
                dest = -1

            d = 4

            if opscode == 99:
                break
            elif opscode == 1:
                states[dest] = param1 + param2
            elif opscode == 2:
                states[dest] = param1 * param2
            elif opscode == 3:
                v = self.iF()

                states[states[pos + 1] + (rbase if tmode[-3] == '2' else 0)] = int(v)

                d = 2

            elif opscode == 4:
                self.oF(param1)
                d = 2

            elif opscode == 5:
                if param1 != 0:
                    d = 0
                    pos = param2
                else:
                    d = 3

            elif opscode == 6:
                if param1 == 0:
                    d = 0
                    pos = param2
                else:
                    d = 3

            elif opscode == 7:
                states[dest] = 1 if param1 < param2 else 0

            elif opscode == 8:
                states[dest] = 1 if param1 == param2 else 0

            elif opscode == 9:
                rbase += param1
                d = 2

            else:
                print("!!!")
                print(opscode)
                break

            pos += d
