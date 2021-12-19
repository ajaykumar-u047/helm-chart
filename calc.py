from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/calc')
def calc():
    return render_template('form.html')

@app.route('/')
def welcome():
    return "<TITLE>Calculator</TITLE><><style> h1 {text-align: center;} p {text-align: center;} h3{text-align: center;} </style> <h1>Welcome to the Simple Calculator App</h1> <p><h3>Add /calc to proceed to the calculator page</h3></p>"



@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
        result = var_1 / var_2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0', port = 5001)
