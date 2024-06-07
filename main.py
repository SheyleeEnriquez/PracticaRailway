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
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f0f0f0;
                }
                .container {
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                label, input {
                    display: block;
                    margin-bottom: 10px;
                }
                input[type="submit"] {
                    padding: 10px 15px;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
                .error {
                    color: red;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <form action="/square" method="post">
                    <label for="number">Ingrese un número:</label>
                    <input type="text" id="number" name="number">
                    <input type="submit" value="Enviar">
                </form>
            </div>
        </body>
        </html>
    ''')

@app.route('/square', methods=['POST'])
def square():
    number_str = request.form['number']
    if not number_str.isdigit():
        return render_template_string('''
            <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-color: #f0f0f0;
                    }
                    .container {
                        background: white;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }
                    .error {
                        color: red;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <p class="error">Por favor, ingrese un número válido.</p>
                    <a href="/">Intentar de nuevo</a>
                </div>
            </body>
            </html>
        ''')

    number = int(number_str)
    result = number ** 2
    return render_template_string('''
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f0f0f0;
                }
                .container {
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                a {
                    display: inline-block;
                    margin-top: 20px;
                    text-decoration: none;
                    padding: 10px 15px;
                    background-color: #007bff;
                    color: white;
                    border-radius: 5px;
                }
                a:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <p>El cuadrado de {{ number }} es {{ result }}.</p>
                <a href="/">Probar otro número</a>
            </div>
        </body>
        </html>
    ''', number=number, result=result)

if __name__ == '__main__':
    port = int(os.getenv("PORT", default=5000))
    app.run(debug=True, host='0.0.0.0', port=port)
