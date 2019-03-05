def lottery(num_colors, num_bperc, filename):
    file_obj = open(filename, "r")

    #setup
    colorlist = []
    totallist = []
    for line in file_obj.readlines():
        x = line.split()
        if x[1] not in colorlist:
            colorlist.append(x[1])
        totallist.append(x)

    #setup counter class
    #instance variable position
    #class method advance
    class Counter:
        def __init__(self, m):
            self.position = 0
            #m = number of numbers per color
            self.m = m
            self.resetnum = 0
            self.atreset = True
        def advance(self):
            self.atreset = False
            self.position = (self.position + 1)%self.m
            if self.position == 0:
                self.resetnum += 1
        def beenReset(self):
            return self.resetnum
        def atReset(self):
            return self.atreset
        def getPos(self):
            return self.position
        def __str__(self):
            return str(self.position)

    def testcounter(list, m, n):
        for i in range(n):
            list.append(Counter(m))
        #print(list[0], " ", list[1], " ", list[2])

    #testcounter([], 3, 3)


    #bycolor contains a list with all the numbers of that color
    #counterray is initialized here with one 0 for every color
    counterray = []
    bycolor = []
    for k in colorlist:
        bycolor.append([])

    for i in range(len(totallist)):
        for j in range(len(colorlist)):
            if int(totallist[i][1]) == j:
                bycolor[j].append(int(totallist[i][0]))

    m = len(bycolor[0])
    for g in bycolor:
        counterray.append(Counter(m))
    #counterray section => finding all possible combinations
        #make measurable returns the list in a way that's readable (non objects)
    def listtonums(list):
        for i in range(len(list)):
            list[i] = list[i].getPos()

    #ATTEMPT NUMBER TWO
    numshifts = 0
    lent = len(counterray)
    chainlist = []
    while counterray[0].beenReset() == 0:
        #print(numshifts)
        #print("[", counterray[0].getPos(), ",", counterray[1].getPos(), ",", counterray[2].getPos(), "]")

        amendment = []
        for w in range(lent):
            amendment.append(bycolor[w][counterray[w].getPos()])

        chainlist.append(amendment)



        counterray[lent-1].advance()
        numshifts += 1

        i = 1
        while i <= lent:
            if numshifts%(m**i) == 0:
                counterray[lent-i-1].advance()
            i += 1


    minimum = max(chainlist[0]) - min(chainlist[0])
    minindex = 0
    for r in range(len(chainlist)):
        current = max(chainlist[r]) - min(chainlist[r])
        if current < minimum:
            minimum = current
            minindex = r


    winner = chainlist[minindex]
    for u in range(len(winner)):
        winner[u] = str(winner[u])
    print(" ".join(winner))

lottery(4,4,"lotteryinput")

