from uuid import uuid4
from django.http import HttpResponse
from rest_framework.views import APIView

from demo.utils.Blockchain import Blockchain
import json

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


class BlockList(APIView):
    # 返回整个区块链
    def get(self, request):
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain),
        }
        return HttpResponse(json.dumps(response))

    # 请求服务器挖掘新的区块
    def post(self, request):
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


class BlockDetail(APIView):
    def get(self, request):
        return None
