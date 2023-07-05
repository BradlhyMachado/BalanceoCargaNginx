from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '1 Ingresa los números en la URL en el siguiente formato: /suma?num1=5&num2=3'

@app.route('/suma')
def suma():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    resultado = num1 + num2
    return "Nodo1       La Suma es: " + str(resultado)

@app.route('/resta')
def resta():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    resultado = num1 - num2
    return "Nodo1       La resta es: " + str(resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)