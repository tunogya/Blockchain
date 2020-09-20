from uuid import uuid4
from django.http import HttpResponse
from demo.utils.Blockchain import Blockchain
import json

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


# 告诉服务器去挖掘新的区块
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


# 创建一个交易并添加到区块
def new_transaction(request):
    values = json.loads(request.body.decode('utf-8'))
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values'
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    print(index)
    response = {'message': 'Transaction will be added to Block %s' % index}
    return HttpResponse(json.dumps(response))


# 返回整个区块链
def full_chain(request):
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return HttpResponse(json.dumps(response))


# 注册节点
def register_nodes(request):
    return None


# 解决冲突
def consensus(request):
    return None
