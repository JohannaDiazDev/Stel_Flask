from flask import Flask, render_template, url_for

app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

if __name__ == '__main__':
    app.run(debug=True)