from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = ",0.95swlb43m8;pnd["

@app.route('/')
def onStart():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def processForm():
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['languages'] = request.form['languages']
    session['comments'] = request.form['comments']

    print(session)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug = True)