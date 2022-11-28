from flask import Flask,render_template,redirect,request,url_for
import re

app = Flask(__name__)
app.secret_key = 'validator'


@app.route('/',methods = ['POST','GET'])
def validator():
    if request.method == 'POST' and 'password' in request.form:
        password  = request.form['password']
        pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        condition = re.match(pattern,password)
        if condition:
            msg = "Password is valid"
            return render_template('index.html',msg=msg)
        else:
            msg = "password is not valid"
            return render_template('index.html',msg=msg)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


