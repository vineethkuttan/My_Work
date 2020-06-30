from random import  randrange
class Vineeth:
    def __init__(self,n,k):
        with open('templates/src.txt', 'r') as fp:
            li1=fp.readlines()
        with open('templates/src2.txt', 'r') as fp:
            self.ansli1=fp.readlines()
        li3=['      </table>\n<br><br>','      <button type="submit" value="submit">Submit</button><br><br>\n','      </form>\n','    <form name="passdata" action="/answer" method="post">\n','<button type="submit" value="submit">Answer</button>\n', '    </div>\n', '  </body>\n', '</html>']
        self.ansli3=li3[:]
        self.ansli3.pop(1)
        self.ansli3.pop(1)
        self.ansli3.pop(1)
        self.ansli3.pop(1)
        self.ansli3.insert(1, '        <button type="submit" value="Restart">Restart</button>')
        self.ansli3.insert(1,'    <form name="passdata" action="/restart" method="post">\n')
        li2=[]
        self.N = n
        self.mat = []
        self.SRN = int(self.N ** 0.5)
        for i in range(self.N):
            self.mat.append([-1 for j in range(self.N)])
        self.K = k
        self.fillValues()
        #fp = open("templates/check1.html", 'w')
        c = 0
        self.track = []
        for i in self.mat:
            li2.append('        <tr>\n')
            for j in i:
                if j != 0:
                    st = f'          <td><input id="cell-{str(c)}"  type="text" value="{str(j)}" disabled></td>\n'
                else:
                    s = 'name="' + str(c) + '"'
                    st = f'          <td><input id="cell-{str(c)}"  {s} type="text"></td>\n'
                    self.track.append(str(c))
                li2.append(st)
                c += 1
            li2.append('        </tr>\n\n\n')
        self.li = li1 + li2 + li3
        #fp.writelines(li)
        #fp.close()
    def answer(self):
        c = 0
        li2=[]
        for i in self.mat:
            li2.append('        <tr>\n')
            for j in i:
                if j != 0:
                    st = f'          <td><input id="cell-{str(c)}"  type="text" value="{str(j)}" disabled></td>\n'
                li2.append(st)
                c += 1
            li2.append('        </tr>\n\n\n')
        self.ans=self.ansli1+li2+self.ansli3

    def fillValues(self):
        self.fillDiagonal()
        self.fillRemaining(0,self.SRN)
        self.answer()
        self.printSudoku(self.mat)
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

    def trcheck(self,tr):
        oo = 0
        ko=range(1,10)
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if self.mat[i][j] == 0:
                    if tr[oo].isnumeric() and int(tr[oo]) in ko and self.issafe(int(tr[oo]), i, j):
                        self.mat[i][j] = int(tr[oo])
                        oo+=1
                    else:
                        return False
        return True

    def printSudoku(self,li):
        for i in range(0, self.N):
            for j in range(0,self.N):
                print(li[i][j],end=" ")
            print()
        print()
