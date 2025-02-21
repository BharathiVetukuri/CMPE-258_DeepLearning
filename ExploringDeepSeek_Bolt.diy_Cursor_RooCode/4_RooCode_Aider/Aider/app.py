from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2 if num2 != 0 else 'Error: Division by zero'
    else:
        return 'Invalid operation'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        operation = request.form.get('operation')
        result = calculate(num1, num2, operation)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
