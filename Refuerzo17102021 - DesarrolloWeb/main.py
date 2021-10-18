#py -m pip install -U pip
#pip install flask

from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/prueba')
def prueba():
    return jsonify({"saludo": "hola"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)