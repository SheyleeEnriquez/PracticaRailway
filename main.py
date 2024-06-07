from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/square', methods=['POST'])
def square():
    number = int(request.form['number'])
    result = number ** 2
    return render_template('result.html', number=number, result=result)

if __name__ == '__main__':
    port = int(os.getenv("PORT", default=5000))
    app.run(debug=True, host='0.0.0.0', port=port)
