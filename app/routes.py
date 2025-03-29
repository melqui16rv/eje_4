from flask import Flask, request, jsonify
from arbol_binario import ArbolBinario

app = Flask(__name__)
arbol = ArbolBinario()

@app.route('/insertar', methods=['POST'])
def insertar():
    data = request.json
    valor = data.get('valor')
    if valor is None:
        return jsonify({"mensaje": "Debe proporcionar un valor"}), 400
    try:
        arbol.insertar(int(valor))
        return jsonify({"mensaje": f"Valor {valor} insertado correctamente"})
    except ValueError:
        return jsonify({"mensaje": "Error: Valor inválido"}), 400

@app.route('/borrar', methods=['POST'])
def borrar():
    arbol.borrar_arbol()
    return jsonify({"mensaje": "Árbol borrado correctamente"})

@app.route('/visualizar', methods=['GET'])
def visualizar():
    try:
        mensaje = arbol.visualizar_arbol()
        return jsonify({"mensaje": mensaje})
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500