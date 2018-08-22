from copy import deepcopy
import time as t
from tkinter import *
'''
S = [[2, 0, 0, 0, 0, 0, 0, 0, 0], # test
     [0, 0, 7, 0, 4, 0, 0, 0, 0],
     [0, 0, 5, 0, 0, 0, 0, 8, 0],
     [1, 0, 0, 0, 3, 0, 0, 2, 0],
     [3, 8, 0, 0, 9, 0, 4, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 0, 7],
     [0, 0, 0, 0, 1, 0, 9, 0, 0],
     [0, 0, 0, 0, 8, 7, 0, 0, 3],
     [4, 0, 3, 0, 0, 9, 5, 0, 0]]

S = [[1, 0, 0, 0, 0, 7, 0, 9, 0], # hardest
     [0, 3, 0, 0, 2, 0, 0, 0, 8],
     [0, 0, 9, 6, 0, 0, 5, 0, 0],
     [0, 0, 5, 3, 0, 0, 9, 0, 0],
     [0, 1, 0, 0, 8, 0, 0, 0, 2],
     [6, 0, 0, 0, 0, 4, 0, 0, 0],
     [3, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 4, 0, 0, 0, 0, 0, 0, 7],
     [0, 0, 7, 0, 0, 0, 3, 0, 0]]

S = [[0, 0, 0, 8, 0, 1, 0, 0, 0], # 17 hints
     [0, 0, 0, 0, 0, 0, 4, 3, 0],
     [5, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 7, 0, 8, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 2, 0, 0, 3, 0, 0, 0, 0],
     [6, 0, 0, 0, 0, 0, 0, 7, 5],
     [0, 0, 3, 4, 0, 0, 0, 0, 0],
     [0, 0, 0, 2, 0, 0, 6, 0, 0]]
'''

def fillPossib(S):
    for i in range(9):
        for j in range(9):
            if S[i][j] == 0:
                S[i][j] = []
                for k in range(1,10):
                    if testLigne(S,i,k) \
                    and testColonne(S,j,k) \
                    and testCarre(S,i,j,k):
                        S[i][j].append(k)

def testLigne(S,i,k):
    if k in S[i]:
        return False
    return True

def testColonne(S,j,k):
    for i in range(9):
        if S[i][j] == k:
            return False
    return True

def testCarre(S,i,j,k):
    if i >= 0 and i <= 2:
        if j >= 0 and j <= 2:
            if k in S[0][0:3] or k in S[1][0:3] or k in S[2][0:3]:
                return False
        elif j >= 3 and j <= 5:
            if k in S[0][3:6] or k in S[1][3:6] or k in S[2][3:6]:
                return False
        else:
            if k in S[0][6:9] or k in S[1][6:9] or k in S[2][6:9]:
                return False

    elif i >= 3 and i <= 5:
        if j >= 0 and j <= 2:
            if k in S[3][0:3] or k in S[4][0:3] or k in S[5][0:3]:
                return False
        elif j >= 3 and j <= 5:
            if k in S[3][3:6] or k in S[4][3:6] or k in S[5][3:6]:
                return False
        else:
            if k in S[3][6:9] or k in S[4][6:9] or k in S[5][6:9]:
                return False

    else:
        if j >= 0 and j <= 2:
            if k in S[6][0:3] or k in S[7][0:3] or k in S[8][0:3]:
                return False
        elif j >= 3 and j <= 5:
            if k in S[6][3:6] or k in S[7][3:6] or k in S[8][3:6]:
                return False
        else:
            if k in S[6][6:9] or k in S[7][6:9] or k in S[8][6:9]:
                return False

    return True

def next(S,i,j):
    j += 1
    if j > 8: j = 0; i += 1
    if i > 8: return 9,0
    while type(S[i][j]) != list:
        j += 1
        if j > 8: j = 0; i += 1
        if i > 8: return 9,0
    return i,j

def prev(S,i,j):
    j -= 1
    if j < 0: j = 8; i -= 1
    while type(S[i][j]) != list:
        j -= 1
        if j < 0: j = 8; i -= 1
    return i,j

def backTrack(S,SPossib):
    i,j = next(SPossib,0,-1)
    while i < 9:
        if S[i][j] == 0:
            ind = 0
        else:
            ind = SPossib[i][j].index(S[i][j])+1
        if ind == len(SPossib[i][j]):
            S[i][j] = 0
            i,j = prev(SPossib,i,j)
        else:
            k = SPossib[i][j][ind]
            if testLigne(S,i,k) \
            and testColonne(S,j,k) \
            and testCarre(S,i,j,k):
                S[i][j] = k
                i,j = next(SPossib,i,j)
            else:
                S[i][j] = k

def printS(S):
    for i in range(9):
        if i == 3 or i == 6:
            print("- - - - - - - - - -")
        for j in range(9):
            if j == 3 or j == 6:
                print("|", end="")
            print(S[i][j], end=" ")
        print("\n")

def clear(sudo):
    for i in range(9):
        for j in range(9):
            sudo.data[i][j].delete(0)
            sudo.data[i][j].configure(fg = 'black')

def resolve(sudo):
    S = []
    for i in range(9):
        s = []
        for j in range(9):
            if sudo.data[i][j].get():
                s.append(int(sudo.data[i][j].get()))
            else:
                s.append(0)
        S.append(s)

    SPossib = deepcopy(S)
    fillPossib(SPossib)
    backTrack(S,SPossib)

    for i in range(9):
        for j in range(9):
            if not sudo.data[i][j].get():
                sudo.data[i][j].delete(0)
                sudo.data[i][j].configure(fg = '#0B0')
                sudo.data[i][j].insert(0, S[i][j])

class IHM(Frame): 
    def __init__(self, fenetre, height, width): 
        Frame.__init__(self, fenetre) 
        self.numberLines = height 
        self.numberColumns = width 
        self.pack(fill=BOTH)

        square1 = Frame(self, bd = 5, bg = 'black')
        square1.grid(row = 0, column = 0)
        square2 = Frame(self, bd = 5, bg = 'black')
        square2.grid(row = 0, column = 1)
        square3 = Frame(self, bd = 5, bg = 'black')
        square3.grid(row = 0, column = 2)
        square4 = Frame(self, bd = 5, bg = 'black')
        square4.grid(row = 1, column = 0)
        square5 = Frame(self, bd = 5, bg = 'black')
        square5.grid(row = 1, column = 1)
        square6 = Frame(self, bd = 5, bg = 'black')
        square6.grid(row = 1, column = 2)
        square7 = Frame(self, bd = 5, bg = 'black')
        square7.grid(row = 2, column = 0)
        square8 = Frame(self, bd = 5, bg = 'black')
        square8.grid(row = 2, column = 1)
        square9 = Frame(self, bd = 5, bg = 'black')
        square9.grid(row = 2, column = 2)

        self.data = list()
        for i in range(0,3):
            line = list()
            for j in range(self.numberColumns):
                if j//3 == 0:
                    square = square1
                elif j//3 == 1:
                    square = square2
                else:
                    square = square3
                cell = Entry(square, width = 2, justify = CENTER, font = 'arial 50')
                line.append(cell)
                cell.grid(row = i, column = j)
            self.data.append(line)

        for i in range(3,6):
            line = list()
            for j in range(self.numberColumns):
                if j//3 == 0:
                    square = square4
                elif j//3 == 1:
                    square = square5
                else:
                    square = square6
                cell = Entry(square, width = 2, justify = CENTER, font = 'arial 50')
                line.append(cell)
                cell.grid(row = i, column = j)
            self.data.append(line)

        for i in range(6,9):
            line = list()
            for j in range(self.numberColumns):
                if j//3 == 0:
                    square = square7
                elif j//3 == 1:
                    square = square8
                else:
                    square = square9
                cell = Entry(square, width = 2, justify = CENTER, font = 'arial 50')
                line.append(cell)
                cell.grid(row = i, column = j)
            self.data.append(line)

# GUI
top = Tk()
top.title('Sudoku solver')
top.iconbitmap("logo.ico")
top.resizable(width = False, height = False)

sudo = IHM(top, 9, 9)
clearButton = Button(top, text = 'Clear', font = 'arial 20 bold', command = lambda: clear(sudo))
clearButton.pack(side = RIGHT)
solve = Button(top, text = 'Solve', font = 'arial 20 bold', command = lambda: resolve(sudo))
solve.pack(side = RIGHT)

top.mainloop()