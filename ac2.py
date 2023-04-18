from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

clientes = [
    {'id': 1, 'nome': 'João', 'email': 'joao@example.com'},
    {'id': 2, 'nome': 'Maria', 'email': 'maria@example.com'},
    {'id': 3, 'nome': 'Pedro', 'email': 'pedro@example.com'}
]

print(len(clientes))

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    response = {'clientes': clientes}
    return jsonify(response), 200


@app.route('/busca/<int:id>/')
def get_busca(id):
    cliente = next((c for c in clientes if c['id'] == id), None)
    if cliente:
        return jsonify(cliente), 200
    else:
        return jsonify({'error': 'Cliente não encontrado'}), 404


@app.route('/api/busca', methods=["GET"])
def get_cliente():
    id = request.args.get("id")
    cliente = next((c for c in clientes if c['id'] == int(id)), None)
    if cliente:
        return jsonify(cliente), 200
    else:
        return jsonify({'error': 'Cliente não encontrado'}), 404


if __name__ == '__main__':
    app.run(debug=True)
