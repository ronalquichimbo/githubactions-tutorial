from flask import Flask

import requests

app = Flask(__name__)

@app.route('/<num1>/<num2>/<op>')
def default(num1, num2, op):
    result = ''
    if op == '+':
        result = requests.get('http://sum:5000/' + num1 + '/' + num2).text
    elif op == '-':
        result = requests.get('http://res:5000/' + num1 + '/' + num2).text
    elif op == '*':
        result = requests.get('http://mul:5000/' + num1 + '/' + num2).text
    elif op == '÷':
        result = requests.get('http://div:5000/' + num1 + '/' + num2).text
    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


