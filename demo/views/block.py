from uuid import uuid4
from django.http import HttpResponse, JsonResponse
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
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        response = {
            'chain': serializer.data,
            'length': Block.objects.all().count(),
        }
        return HttpResponse(json.dumps(response))

    # 请求服务器挖掘新的区块
    def post(self, request):
        last_block = blockchain.last_block
        last_proof = last_block['proof']
        proof = blockchain.proof_of_work(last_proof)
        print(proof)
        # 创建新的区块
        this_block = blockchain.new_block(proof=proof)
        # 将区块保存到数据库
        _block = Block(
            index=this_block['index'],
            hash=blockchain.hash(this_block),
            previous_hash=this_block['previous_hash'],
            create_time=this_block['create_time'],
            transactions=this_block['transactions'],
            proof=this_block['proof'],
        )
        try:
            _block.save()
        except Exception as e:
            print(str(e))
            return False

        response = {
            'message': "New Block Forged",
            'index': this_block['index'],
            'transactions': this_block['transactions'],
            'proof': this_block['proof'],
            'previous_hash': this_block['previous_hash'],
        }
        print(response)
        return JsonResponse(response)


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
