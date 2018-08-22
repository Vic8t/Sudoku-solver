S = [[2, 0, 0, 0, 0, 0, 0, 0, 0], # test
     [0, 0, 7, 0, 4, 0, 0, 0, 0],
     [0, 0, 5, 0, 0, 0, 0, 8, 0],
     [1, 0, 0, 0, 3, 0, 0, 2, 0],
     [3, 8, 0, 0, 9, 0, 4, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 0, 7],
     [0, 0, 0, 0, 1, 0, 9, 0, 0],
     [0, 0, 0, 0, 8, 7, 0, 0, 3],
     [4, 0, 3, 0, 0, 9, 5, 0, 0]]
'''
S = [[0, 6, 2, 0, 5, 0, 4, 7, 0], # test
     [0, 8, 0, 0, 0, 0, 9, 0, 0],
     [5, 0, 0, 0, 0, 2, 0, 0, 6],
     [0, 0, 0, 1, 6, 0, 0, 0, 0],
     [6, 1, 0, 0, 0, 0, 0, 9, 3],
     [0, 0, 0, 0, 8, 5, 0, 0, 0],
     [7, 0, 0, 2, 0, 0, 0, 0, 9],
     [0, 0, 8, 0, 0, 0, 0, 4, 0],
     [0, 9, 4, 0, 1, 0, 2, 6, 0]]

S = [[1, 0, 0, 0, 0, 7, 0, 9, 0], # hardest
     [0, 3, 0, 0, 2, 0, 0, 0, 8],
     [0, 0, 9, 6, 0, 0, 5, 0, 0],
     [0, 0, 5, 3, 0, 0, 9, 0, 0],
     [0, 1, 0, 0, 8, 0, 0, 0, 2],
     [6, 0, 0, 0, 0, 4, 0, 0, 0],
     [3, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 4, 0, 0, 0, 0, 0, 0, 7],
     [0, 0, 7, 0, 0, 0, 3, 0, 0]]

S = [[0, 0, 0, 9, 3, 0, 0, 4, 0], # very hard
     [0, 5, 0, 0, 7, 0, 0, 2, 3],
     [0, 0, 0, 0, 0, 5, 6, 0, 0],
     [1, 0, 0, 3, 0, 0, 2, 0, 0],
     [8, 9, 0, 0, 0, 0, 0, 5, 6],
     [0, 0, 7, 0, 0, 6, 0, 0, 8],
     [0, 0, 9, 7, 0, 0, 0, 0, 0],
     [7, 4, 0, 0, 9, 0, 0, 6, 0],
     [0, 8, 0, 0, 5, 3, 0, 0, 0]]
'''
def transList():
    for i in range(9):
        for j in range(9):
            if S[i][j] == 0:
                S[i][j] = []

def testLigne(i,k):
    if k in S[i]:
        return False
    return True

def testColonne(j,k):
    for i in range(9):
        if S[i][j] == k:
            return False
    return True

def testCarre(i,j,k):
    if i >= 0 and i <= 2:
        if j >= 0 and j <= 2:
            if k in S[0][0:3] or k in S[1][0:3] or k in S[2][0:3]:
                return False
        if j >= 3 and j <= 5:
            if k in S[0][3:6] or k in S[1][3:6] or k in S[2][3:6]:
                return False
        if j >= 6 and j <= 8:
            if k in S[0][6:9] or k in S[1][6:9] or k in S[2][6:9]:
                return False

    if i >= 3 and i <= 5:
        if j >= 0 and j <= 2:
            if k in S[3][0:3] or k in S[4][0:3] or k in S[5][0:3]:
                return False
        if j >= 3 and j <= 5:
            if k in S[3][3:6] or k in S[4][3:6] or k in S[5][3:6]:
                return False
        if j >= 6 and j <= 8:
            if k in S[3][6:9] or k in S[4][6:9] or k in S[5][6:9]:
                return False

    if i >= 6 and i <= 8:
        if j >= 0 and j <= 2:
            if k in S[6][0:3] or k in S[7][0:3] or k in S[8][0:3]:
                return False
        if j >= 3 and j <= 5:
            if k in S[6][3:6] or k in S[7][3:6] or k in S[8][3:6]:
                return False
        if j >= 6 and j <= 8:
            if k in S[6][6:9] or k in S[7][6:9] or k in S[8][6:9]:
                return False

    return True

def fillList():
    for i in range(9):
        for j in range(9):
            if type(S[i][j]) == list:
                S[i][j] = []
                for k in range(1,10):
                    if testLigne(i,k) and testColonne(j,k) and testCarre(i,j,k):
                        S[i][j].append(k)

def printS(S):
    for i in range(9):
        if i == 3 or i == 6:
            print("- - - - - - - - - -")
        for j in range(9):
            if j == 3 or j == 6:
                print("|", end="")
            print(S[i][j], end=" ")
        print("\n")

def notComplete():
    for i in range(9):
        for j in range(9):
            if type(S[i][j]) == list:
                return True
    return False

def numberFound():
    for i in range(9):
        for j in range(9):
            if type(S[i][j]) == list and len(S[i][j]) == 1:
                S[i][j] = S[i][j][0]

def notInLine(i,j,k):
    for j2 in range(9):
        if j2 != j and type(S[i][j2]) == list and k in S[i][j2]:
            return False
    return True

def notInColumn(i,j,k):
    for i2 in range(9):
        if i2 != i and type(S[i2][j]) == list and k in S[i2][j]:
            return False
    return True

def deduce():
    for i in range(9):
        for j in range(9):
            if type(S[i][j]) == list:
                for elt in S[i][j]:
                    if notInLine(i,j,elt) or notInColumn(i,j,elt):
                        S[i][j] = [elt]

def resolve(S):
    limit = 0
    transList()
    while limit < 100 and notComplete():
        fillList()
        deduce()
        numberFound()
        limit += 1
    printS(S)
    if limit >= 100:
        print("No solution found")

# Main
resolve(S)