import json
from uuid import uuid4
from django.http import HttpResponse
from utils.Blockchain import Blockchain

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()


def mine(request):
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    print(proof)
    blockchain.new_transaction(
         sender="0",
         recipient=node_identifier,
         amount=1,
     )

    # Forge the new Block by adding it to the chain
    block = blockchain.new_block(proof)

    response = {
         'message': "New Block Forged",
         'index': block['index'],
         'transactions': block['transactions'],
         'proof': block['proof'],
         'previous_hash': block['previous_hash'],
    }
    print(response)
    return HttpResponse(json.dumps(response))


def new_transaction(request):
    values = json.loads(request.body.decode('utf-8'))
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values'
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    print(index)
    response = {'message': 'Transaction will be added to Block %s'%index}
    return HttpResponse(json.dumps(response))


def full_chain(request):
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return HttpResponse(json.dumps(response))