from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <form action="/square" method="post">
            <label for="number">Ingrese un número:</label>
            <input type="text" id="number" name="number">
            <input type="submit" value="Enviar">
        </form>
    ''')

@app.route('/square', methods=['POST'])
def square():
    number_str = request.form['number']
    if not number_str.isdigit():
        return render_template_string('''
            <p>Por favor, ingrese un número válido.</p>
            <a href="/">Intentar de nuevo</a>
        ''')
    
    number = int(number_str)
    result = number ** 2
    return render_template_string('''
        <p>El cuadrado de {{ number }} es {{ result }}.</p>
        <a href="/">Probar otro número</a>
    ''', number=number, result=result)

if __name__ == '__main__':
    port = int(os.getenv("PORT", default=5000))
    app.run(debug=True, host='0.0.0.0', port=port)
