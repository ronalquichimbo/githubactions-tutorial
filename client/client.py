from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def route():
    return render_template('view.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
    op = request.form['action']
    num1 = request.form['num1']
    num2 = request.form['num2']
    result = requests.get('http://app:5000/' + num1 + '/' + num2 + '/' + op).text
    return render_template('view.html', resultado_op = result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)