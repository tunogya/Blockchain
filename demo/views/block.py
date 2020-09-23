from uuid import uuid4
from django.http import HttpResponse
from rest_framework import mixins
from rest_framework import generics
from demo.serializers import BlockSerializer

from demo.utils.Blockchain import Blockchain
import json
from demo.models.block import Block

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


class BlockList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView,):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
    filterset_fields = ['index', 'hash', 'previous_hash', 'create_time', 'transactions', 'proof']

    # 返回整个区块链
    def get(self, request, *args, **kwargs):
        chain = self.list(request, *args, **kwargs)
        response = {
            'chain': chain,
            'length': Block.objects.all().count(),
        }
        return HttpResponse(json.dumps(response))

    # 请求服务器挖掘新的区块
    def post(self, request):
        last_block = blockchain.last_block
        last_proof = last_block['proof']
        proof = blockchain.proof_of_work(last_proof)
        print(proof)
        state = "VALID"
        events = []
        data = ""
        blockchain.new_transaction(
            state=state,
            events=events,
            data=data,
        )

        # Forge the new Block by adding it to the chain
        block = blockchain.new_block(proof=proof)

        response = {
            'message': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
        }
        print(response)
        return HttpResponse(json.dumps(response))


class BlockDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    serializer_class = BlockSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
