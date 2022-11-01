from flask import Flask, render_template, request, jsonify
import os
import predictions

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        dados = [
            float(request.form['comp_sep']),
            float(request.form['larg_sep']),
            float(request.form['comp_petala']),
            float(request.form['larg_petala'])
        ]

        y_pred = predictions.predict(dados)

        return jsonify({"Setosa": f'{y_pred[0]}',
                        "Versicolor": f'{y_pred[1]}',
                        "Virginica": f'{y_pred[2]}'
                        })
    elif request.method == 'GET':
        return jsonify({"messagem": "Utilize o formulário"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
