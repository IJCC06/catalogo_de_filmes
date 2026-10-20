from flask import Flask, request, jsonify
from database import criar_conexao

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World!</h1>"


@app.route('/usuario', methods=['GET'])
def buscar_usuario():
    usuario = {
        "nome": "Gabriel",
        "idade": 16,
        "telefone": "(19) 998174818"
    }
    return usuario


@app.route('/filme', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados Inválidos"}), 400

    print(f"Novo Filme: {dados}")

    conn = criar_conexao()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO filmes (
            id_usuario,
            titulo,
            ano_lancamento,
            genero,
            nota,
            capa_url)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id_filmes
    """, (dados['usuario_id'], dados['titulo'], dados['ano_lancamento'], dados['genero'],
          dados['nota'], dados['capa_url']))

    novo_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    return jsonify({
        "message": "Filme Salvo com Sucesso!",
        "filme_id": novo_id
    }), 201


@app.route('/produto', methods=['PUT'])
def atualizar_produto():
    produto = {
        "id": 1,
        "nome": "Caneta Azul",
        "preco": 1.50,
        "descricao": "Caneta esferográfica de cor azul",
        "marca": "Bic"
    }
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    if dados['id'] == produto['id']:
        produto = dados
        print(f"Produto Atualizado: {produto}")
        return jsonify({"message": "Produto Atualizado com sucesso!"}), 201
    else:
        return jsonify({"message": "Produto não Encontrado!"}), 404


@app.route('/teste/db', methods=['GET'])
def testar_conexao():
    conn = criar_conexao()
    print('Testando conexão: ', conn)
    conn.close()
    return jsonify({"message": "Banco conectado com sucesso!"}), 200


if __name__ == "__main__":
    app.run(debug=True)