from flask import Flask
from flask import jsonify
import requests

controller = Flask(__name__)
@controller.route('/clima/<cidade>/<uf>', methods=['GET'])
def buscarClima(cidade, uf):
    minha_chave = 'dc63543f'
    url = f'https://api.hgbrasil.com/weather?key={minha_chave}&city_name={cidade},{uf}'

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        resposta = {"cidade": dados["results"]["city_name"],
                    "data": dados["results"]["date"],
                    "descricao": dados["results"]["description"],
                    "temperatura": dados["results"]["temp"],
                    "umidade": dados["results"]["humidity"],
                    "probChuva": dados["results"]["forecast"][0]["rain_probability"]}
        return jsonify(resposta)
    else:
        return f'Erro ao buscar dados do clima. Código de status: {response.status_code}'

controller.run(port=5000, host='192.168.156.9', debug=True) #aqui é necessário colocar o IP que a máquina está no momento

# Press the green button in the gutter to run the script.