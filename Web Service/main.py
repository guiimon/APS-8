from flask import Flask, request, jsonify
import requests


controller = Flask(__name__)
@controller.route('/clima/<cidade>/<uf>', methods=['GET'])
def buscarClima(cidade, uf):
    minha_chave = 'dc63543f'
    url = f'https://api.hgbrasil.com/weather?key={minha_chave}&city_name={cidade},{uf}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return f'Erro ao buscar dados do clima. Código de status: {response.status_code}'

controller.run(port=5000, host='192.168.39.9', debug=True)

# Press the green button in the gutter to run the script.