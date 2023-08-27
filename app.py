import os 
from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.app_context().push()
last_20 = []

@app.route('/<path:exp>',methods=['GET','POST'])
def calc(exp):
    print(exp)
    ans = None
    ques = None
    ls = exp.split('/')
    print(ls)
    s = ""
    for x in ls :
        if x == "minus":
            s = s+'-'
        elif x == "plus":
            s = s+'+'
        elif x == "into":
            s = s+'*'
        elif x == "by":
            s = s+'/'
        else:
            s=s+x
    n= eval(s)
    dic= {'question': s, 'answer': n}
    last_20.insert(0,dic)
    c=0
    with open('./data.txt', "w") as file:
        for item in last_20:
            file.write(str(item) + "\n") 
            c=c+1
            if c>=20:
                break 
    return jsonify(dic)

@app.route('/history',methods=["GET"])
def history():
    print(last_20)
    lss =[]
    with open('./data.txt', "r") as file:
        for line in file:
            data = eval(line)
            lss.append(data)
    return jsonify(lss)

if __name__ == "__main__":
    app.run(debug=True, port='2000' )
