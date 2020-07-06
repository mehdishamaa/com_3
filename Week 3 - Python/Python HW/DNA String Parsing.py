

class string_counter:
    def counter(self):
        string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        A = 0
        G = 0
        C = 0
        T = 0

        for n in string:
            if n == "A":
                A += 1
            elif n == "G":
                G += 1
            elif n == "C":
                C += 1
            elif n == "T":
                T += 1

        print("A:".format(A))
        print("C:".format(G))
        print("G:".format(C))
        print("T:".format(T))


TestFunction = string_counter()
TestFunction.counter()



















