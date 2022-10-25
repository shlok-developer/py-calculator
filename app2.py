from flask import Flask , render_template, request
app= Flask(__name__)


def multiply(a,b):
    ans= int(a) * int(b)
    return ans
def division(a,b):
    ans= int(a)/ int(b)
    return ans
def addition(a,b):
    ans= int(a) +int(b) 
    return ans
def substraction(a,b):
    ans= int(a)-int(b)
    return ans


@app.route('/', methods=['GET','POST'])
def home():

    if request.method=='POST':

        num1=request.form['num1']
        num2=request.form['num2']

        if request.form['ops']=='multiply':
            ans=multiply(a=num1, b=num2)
            return render_template('index.html' , ans=ans)

        if request.form['ops']=='addition':
            ans=addition(a=num1, b=num2)
            return render_template('index.html' , ans=ans)

        if request.form['ops']=='substraction':
            ans=substraction(a=num1, b=num2)
            return render_template('index.html', ans=ans)

        if request.form['ops']=='division':
            ans=division(a=num1, b=num2)
            return render_template('index.html', ans=ans)

    return render_template('index.html')

app.run(debug=True)

