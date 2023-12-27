import requests
from flask import Flask, jsonify
from bd import Carros

app = Flask(__name__)


@app.route('/carros', methods=['GET'])
def get_carros():
    carro_json = jsonify({"carros": Carros})
    return carro_json



@app.route("/carros/<int:id>", methods=["GET"])
def obter_carro(id):
    carro_encontrado = next((vazio for carro in Carros if carro.get('ID') == id), None)
    if carro_encontrado:
        return jsonify(carro_encontrado)
    return jsonify({"mensagem": "Carro não encontrado"}), 404




app.run()