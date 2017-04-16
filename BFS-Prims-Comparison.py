'''
QUEEN'S UNIVERSITY
CISC 235 2015W
Assignment 4
Brianna Rubin
'''

import random

def makeGraph():
    G = [[0 for x in range(7)] for x in range(7)]

    n = 6

    G[1] = [0,0,15,0,7,10,0]
    G[2] = [0,15,0,9,11,0,9]
    G[3] = [0,0,9,0,0,12,7]
    G[4] = [0,7,11,0,0,8,14]
    G[5] = [0,10,0,12,8,0,8]
    G[6] = [0,0,9,7,14,8,0]
    return G

def randomGraph(n):
    G = [[0 for x in range(n+1)] for x in range(n+1)]
    vertices = range(1,n+1)
    for i in range(2,n+1):
        x = random.randint(0,i-1)
        S = []
        for j in range(x):
            S.append(random.randint(1,i))
            for s in S:
                w = random.randint(10,100)
                G[i][s] = w
                G[s][i] = w
    for i in range(len(G)):
        G[i][i] = 0



    return G



def BFS(G,v):
    visited = []
    n = 6
    totalWeight = 0
    Q = []
    visited.append(v)
    Q.append(v)
    while len(Q) != 0:
        x = Q[0]
        Q.remove(x)
        for i in range(1,7):
            y = G[x][i]

            if (i not in visited) and (y > 0):
                tuple =  (x,i,y)
                z = tuple[1]
                visited.append(z)
                Q.append(z)
                totalWeight += y
                print "Vertex ",x, " is the parent of Vertex ", i, " with a weight of ",y
    print ""
    print "Total Weight of Tree: ", totalWeight

def Prims(G,v):
    visited = []
    n = 6
    totalWeight = 0
    V = []
    for i in range (1,len(G)):
        V.append(i)
    A = []
    Va = [v]
    Vr =  []
    for i in V:
        if i != v:
            Vr.append(i)

    while len(A) < (n-1):
        for v in Va:
            neighbors = G[v]
            cost = []
            index = []
            for i in range(len(neighbors)):
                if G[v][i] != 0:
                    if i not in Va:
                        cost.append(G[v][i])
                        index.append(i)
        z = min(cost)
        i = cost.index(z)
        y = index[i]
        e = (v,y,z)
        A.append(e)
        Va.append(y)
        totalWeight += z
        print "Vertex ",v, " is the parent of Vertex ",y, " with a weight of ", z
    print ""
    print "Total Weight of Tree: ", totalWeight


def BFS2(G,n,v):
    visited = []
    totalWeight = 0
    Q = []
    visited.append(v)
    Q.append(v)
    while len(Q) != 0:
        x = Q[0]
        Q.remove(x)
        for i in range(1,len(G)):
            y = G[x][i]

            if (i not in visited) and (y > 0):
                tuple =  (x,i,y)
                z = tuple[1]
                visited.append(z)
                Q.append(z)
                totalWeight += y
    #print "Total Weight of Tree: ", totalWeight
    return totalWeight

def Prims2(G,n,v):

    visited = []
    n = 6
    totalWeight = 0
    V = []
    for i in range (1,len(G)):
        V.append(i)
    A = []
    Va = [v]
    Vr =  []
    for i in V:
        if i != v:
            Vr.append(i)

    while len(A) < (n-2):
        for v in Va:
            neighbors = G[v]
            cost = []
            index = []
            for i in range(1,len(neighbors)):
                if G[v][i] != 0:
                    if i not in Va:
                        cost.append(G[v][i])
                        index.append(i)
            if len(cost) != 0:
                z = min(cost)
                i = cost.index(z)
                y = index[i]
            e = (v,y,z)

            if y not in Va:
                A.append(e)
                Va.append(y)
                Vr.remove(y)
                totalWeight += z
    return totalWeight

def Part1():
    G = makeGraph()
    v = 1
    print "***************  Part 1: BFS ***************"
    print ""
    BFS(G,v)
    print ""

def Part2():
    G = makeGraph()
    v = 1
    print "***********  Part 2: PRIMS MST  ************"
    print ""
    Prims(G,v)
    print ""

def Part3():
    print"****************  Part 3  ****************"
    ns = [100,200,300,400,500]
    for n in ns:
        print "n = ",n
        ratios = []
        totalRatio = 0.000
        for i in range(1,10):
            G = randomGraph(n)
            v = random.randint(1,n)
            BFSTotalWeight = BFS2(G,n,v)
            PrimsTotalWeight = Prims2(G,n,v)
            ratio = float(PrimsTotalWeight)/BFSTotalWeight
            ratios.append(ratio)
        for r in ratios:
            totalRatio += r
            aveRatio = totalRatio/len(ratios)
        print "Average Ratio: ",aveRatio


Part1()
Part2()
Part3()
