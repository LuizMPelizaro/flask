from socket import J1939_NLA_BYTES_ACKED
from tkinter.messagebox import RETRY
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        return jsonify(request.form)
    return jsonify({"messagem": "Utilize o formulário"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
