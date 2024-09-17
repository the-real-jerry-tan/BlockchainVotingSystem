"""
 * © 2024 Jerry Tan. All Rights Reserved.
 *
 * This software is the confidential and proprietary information of Jerry Tan
 * ("Confidential Information"). You shall not disclose such Confidential Information
 * and shall use it only in accordance with the terms under which this software
 * was distributed or otherwise published, and solely for the prior express purposes
 * explicitly communicated and agreed upon, and only for those specific permissible purposes.
 *
 * This software is provided "AS IS," without a warranty of any kind. All express or implied
 * conditions, representations, and warranties, including any implied warranty of merchantability,
 * fitness for a particular purpose, or non-infringement, are disclaimed, except to the extent
 * that such disclaimers are held to be legally invalid.
 *
 * This file sets up the server that handles voting via HTTP endpoints.
"""

from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/vote', methods=['POST'])
def vote():
    values = request.get_json()
    required = ['voter_id', 'vote']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new transaction (vote)
    index = blockchain.new_transaction(values['voter_id'], values['vote'])
    response = {'message': f'Your vote will be added to block {index}'}
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    # We need to run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Reward the miner (in this case, there's no currency, so we skip the reward logic)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New block mined',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)
