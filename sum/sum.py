from flask import Flask

app = Flask(__name__)

@app.route("/<num1>/<num2>")
def divide(num1, num2):
    return str(float(num1) + float(num2))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)