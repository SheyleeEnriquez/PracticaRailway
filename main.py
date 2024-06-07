from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    text-align: center;
                }
                label, input {
                    font-size: 20px;
                    margin: 10px 0;
                }
                input[type="submit"] {
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <form action="/square" method="post">
                <label for="number">Ingrese un número:</label>
                <input type="text" id="number" name="number">
                <input type="submit" value="Enviar">
            </form>
        </body>
        </html>
    ''')

@app.route('/square', methods=['POST'])
def square():
    number = int(request.form['number'])
    result = number ** 2
    return render_template_string('''
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    text-align: center;
                }
                p {
                    font-size: 24px;
                }
                a {
                    font-size: 18px;
                    display: block;
                    margin-top: 20px;
                    text-decoration: none;
                    color: #007bff;
                }
            </style>
        </head>
        <body>
            <p>El cuadrado de {{ number }} es {{ result }}.</p>
            <a href="/">Probar otro número</a>
        </body>
        </html>
    ''', number=number, result=result)

if __name__ == '__main__':
    port = int(os.getenv("PORT", default=5000))
    app.run(debug=True, host='0.0.0.0', port=port)
