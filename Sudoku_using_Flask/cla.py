from Sudo import Vineeth as V
from flask import Flask,render_template,request
app=Flask(__name__)
obj=None
@app.route('/')
def sudoku():
    return render_template('EMT.html')
@app.route('/difficult',methods=['POST'])
def diff():
    global  obj
    s1=request.form['dif']
    if s1=='easy':
        n=int((9*9)*0.33)
        obj = V.Vineeth(9,n)
        obj.printSudoku(obj.mat)
        return ''.join(obj.li)
    elif s1=='medium':
        n = int((9 * 9) * 0.5)
        obj = V.Vineeth(9, n)
        obj.printSudoku(obj.mat)
        return ''.join(obj.li)
    else:
        n = int((9 * 9) * 0.66)
        obj = V.Vineeth(9, n)
        obj.printSudoku(obj.mat)
        return ''.join(obj.li)
@app.route('/answer',methods=['POST'])
def answer():
    global obj
    return ''.join(obj.ans)
@app.route('/table',methods=['POST'])
def getdata():
    global obj
    try:
        tr=[]
        for i in obj.track:
            tr.append(request.form[i])
        print(tr)
        if obj.trcheck(tr):
            return render_template('success.html')
        else:
            return render_template('sorry.html')
    except Exception as e:
        return render_template('sorry.html')
@app.route('/restart',methods=['POST'])
def restart():
    return render_template('EMT.html')
if __name__=='__main__':
    app.run(debug=True)