from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Infinity"
        elif operation == "^":
            result = num1 ** num2
        elif operation == "√":
            if num1 >= 0:
                result = num1 ** 0.5
            else:
                result = "Invalid input"
        elif operation == "%":
            result = (num1 / 100) * num2

        return render_template('index.html', result=result)
    except ValueError:
        return render_template('index.html', error="Please enter valid numbers")

if __name__ == '__main__':
    app.run(debug=True)
