from flask import Flask, jsonify, request

app = Flask(__name__)

dados = [
    {"id": 1, "nome": "Item 1"},
    {"id": 2, "nome": "Item 2"},
    {"id": 3, "nome": "Item 3"}
]

@app.route('/itens', methods=['GET'])
def obter_todos():
    return jsonify({"itens": dados})

@app.route('/itens/<int:item_id>', methods=['GET'])
def obter_por_id(item_id):
    item = next((item for item in dados if item['id'] == item_id), None)
    if item:
        return jsonify({"item": item})
    else:
        return jsonify({"mensagem": "Item não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
