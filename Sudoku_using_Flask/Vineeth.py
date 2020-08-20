from random import  randrange
from copy import deepcopy as dc
class Vineeth:
    def __init__(self,n,k):
        self.N = n
        self.mat = []
        self.SRN = int(self.N ** 0.5)
        for i in range(self.N):
            self.mat.append([-1 for j in range(self.N)])
        self.K = k
        self.fillValues()
    def fillValues(self):
        self.fillDiagonal()
        self.fillRemaining(0,self.SRN)
        self.ans=dc(self.mat)
        #self.printSudoku(self.mat)
        self.removeKDigits()
    def fillDiagonal(self):
        for i in range(0,self.N,self.SRN):
            self.fillBox(i, i)
    def  unUsedInBox(self,rowStart,colStart,num):
        for i in range(0,self.SRN):
            for j in range(0,self.SRN):
                if (self.mat[rowStart+i][colStart+j]==num):
                    return False
        return True
    def fillBox(self,row,col):
        for i in range(0,self.SRN):
            for j in range(0, self.SRN):
                num=randrange(1,self.N+1)
                while (not self.unUsedInBox(row, col, num)):
                    num = randrange(1,self.N+1)
                self.mat[row+i][col+j] = num
    def CheckIfSafe(self,i,j,num):
        return (self.unUsedInRow(i, num) and self.unUsedInCol(j, num) and self.unUsedInBox(i-i%self.SRN, j-j%self.SRN, num))
    def unUsedInRow(self,i,num):
        for j in range(0,self.N):
            if (self.mat[i][j] == num):
                return False
        return True
    def unUsedInCol(self,j,num):
        for i in range(0,self.N):
            if (self.mat[i][j] == num):
                return False
        return True
    def fillRemaining(self,i,j):
        if (j>=self.N and i<self.N-1):
            i = i + 1
            j = 0
        if (i>=self.N and j>=self.N):
            return True
        if (i < self.SRN):
            if (j < self.SRN):
                j = self.SRN
        elif (i < self.N-self.SRN):
            if (j==(int)(i/self.SRN)*self.SRN):
                j = j + self.SRN
        else:
            if (j == self.N-self.SRN):
                i = i + 1
                j = 0
                if (i>=self.N):
                    return True
        for num in range(1,self.N+1):
            if (self.CheckIfSafe(i, j, num)):
                self.mat[i][j] = num
                if (self.fillRemaining(i, j+1)):
                    return True
                self.mat[i][j] = 0
        return False
    def issafe(self,n,row,col):
        if(self.mat[row][col]!=0):
            return False
        for i in range(self.N):
            if(self.mat[row][i]==n):
                return False
        for i in range(self.N):
            if(self.mat[i][col]==n):
                return False
        StartRow=row-row%self.SRN
        StartCol=col-col%self.SRN
        for i in range(self.SRN):
            for j in range(self.SRN):
                if(self.mat[i+StartRow][j+StartCol]==n):
                    return False
        return True
    def removeKDigits(self):
        count = self.K
        while (count != 0):
            i = randrange(0,self.N)
            j = randrange(0,self.N)
            if (self.mat[i][j] != 0):
                count-=1
                self.mat[i][j] = 0
    def printSudoku(self,li):
        for i in range(0, self.N):
            for j in range(0,self.N):
                print(li[i][j],end=" ")
            print()
        print()
if __name__=='__main__':
    obj=Vineeth(9,15)
    obj.printSudoku(obj.mat)#Question
    obj.printSudoku(obj.ans) #Answer