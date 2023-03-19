import datetime
import hashlib
import json
from flask import Flask, jsonify


# Criando um blockchain

class Blockchain:
    def __init__ (self):
        # Inicializa a lista que irá armazenar os blocos
        self.chain = []
        # Cria o bloco gênese
        self.create_block(proof = 1, previous_hash='0')
        
    def create_block(self, proof, previous_hash):
        # Cria um bloco e adiciona à cadeia de blocos
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
            }
        self.chain.append(block)
        # Retorna o bloco criado
        return (block)
    
    def get_previous_block(self):
        # Retorna o último bloco adicionado à cadeia
        return (self.chain[-1])
    
    def proof_of_work(self, previous_proof):
        # Realiza o processo de mineração para obter uma prova válida
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return (new_proof)
    
    def hash(self, block):
        # Gera o hash do bloco fornecido
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return (hashlib.sha256(encoded_block).hexdigest())
    
    def is_chain_valid(self, chain):
        # Verifica se a cadeia de blocos é válida
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block ['previous_hash'] != self.hash(previous_block):
                # Verifica se o hash do bloco anterior coincide com o campo previous_hash do bloco atual
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                # Verifica se a prova do bloco atual é válida
                return False
            previous_block = block
            block_index += 1
        # Se todos os blocos foram verificados, a cadeia é válida
        return True
    
# Instanciando a aplicação Flask
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Instanciando a classe Blockchain
blockchain = Blockchain()

# Endpoint para mineração de um novo bloco
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'Parabéns, um bloco foi mineirado!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
        }
    return jsonify(response), 200

# Endpoint para obter a cadeia completa de blocos
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

# Endpoint para verificar se a cadeia de blocos é válida
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'Tudo ok, o Blockchain é válido!'}
    else:
        response = {'message': 'O blockchain não é válido!'}
    return jsonify(response), 200


app.run(host = '0.0.0.0', port=5000)

