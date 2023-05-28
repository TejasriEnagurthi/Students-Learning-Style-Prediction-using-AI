import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import sqlite3

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')

@app.route("/signup")
def signup():

    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return render_template("home.html")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("home.html")
    else:
        return render_template("signup.html")

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]

    # Create a numpy array from the list of input values
    final_features = np.array(int_features).reshape(1, -1)

    # Load the trained model
    model = joblib.load('model.sav')

    # Make predictions on the input data
    predictions = model.predict(final_features)

    # Process the predictions and generate appropriate outputs
    if predictions == 0:
        output = 'Exceptionally Good'
        output1 = 'your skills in all the areas are little low.'
        output2 = 'need to put little efforts to meet the expectations'
    elif predictions == 1:
        output = 'you are incredible'
        output1 = 'your love for learning is impressive'
        output2 = 'Keep on going... Work Hard...'
    elif predictions == 2:
        output = 'you are awesome'
        output1 = 'a consistent efforts is required to achieve the goal'
        output2 = 'wish you all the best'

        # Render the prediction results in a HTML template
    return render_template('prediction.html', output=output, output1=output1, output2=output2)


@app.route('/analysis')
def analysis():
	return render_template('notebook.html')

@app.route('/Learning')
def Learning():
    return render_template('Learning.html')

@app.route('/suggestion')
def suggestion():
    return render_template('suggestion.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/quizzes')
def quizzes():
    return render_template('Quizzes.html')

@app.route('/quiz1')
def quiz1():
    return render_template('quiz1.html')

@app.route('/quiz2')
def quiz2():
    return render_template('quiz2.html')

@app.route('/quiz3')
def quiz3():
    return render_template('quiz3.html')

@app.route('/quiz4')
def quiz4():
    return render_template('quiz4.html')

@app.route('/quiz5')
def quiz5():
    return render_template('quiz5.html')

@app.route('/quiz6')
def quiz6():
    return render_template('quiz6.html')

@app.route('/quiz7')
def quiz7():
    return render_template('quiz7.html')

@app.route('/quiz8')
def quiz8():
    return render_template('quiz8.html')

@app.route('/quiz9')
def quiz9():
    return render_template('quiz9.html')

if __name__ == "__main__":
    app.run(debug=True)
