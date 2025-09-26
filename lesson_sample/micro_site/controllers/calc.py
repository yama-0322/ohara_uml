from flask import Flask, request, render_template_string

app = Flask(__name__)

def calc():
    result = None
    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            result = a + b
        except Exception:
            result = '入力エラー'
    return result

if __name__ == '__main__':
    app.run(debug=True)

