import Vineeth as V
from flask import Flask,render_template,request,redirect
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
        return render_template('ques.html',ques=obj.mat,c=0)
    elif s1=='medium':
        n = int((9 * 9) * 0.5)
        obj = V.Vineeth(9, n)
        return render_template('ques.html', ques=obj.mat, c=0)
    else:
        n = int((9 * 9) * 0.66)
        obj = V.Vineeth(9, n)
        return render_template('ques.html', ques=obj.mat, c=0)
@app.route('/answer',methods=['POST'])
def answer():
    global obj
    return render_template('ans.html',ques=obj.ans,c=0)
@app.route('/table',methods=['POST'])
def getdata():
    global obj
    di=request.form
    f=True
    for i in di.keys():
        row,col=i[0],i[1]
        if di[i]=='':
            k=-1
        else:
            k=int(di[i])
        if k<10 and k>0:
            f=obj.issafe(row,col,k)
        else:
            f=False
        if not f:
            break
    if f:
        return render_template('success.html')
    else:
        return render_template('sorry.html')
@app.route('/restart',methods=['POST'])
def restart():
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)