from uuid import uuid4
from django.http import HttpResponse
from rest_framework.views import APIView

from demo.utils.Blockchain import Blockchain
import json

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


# 交易
class TransactionList(APIView):
    # 返回所有交易
    def get(self, request):
        return None

    # 创建一个交易并添加到区块
    def post(self, request):
        values = json.loads(request.body.decode('utf-8'))
        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return 'Missing values'
        index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
        print(index)
        response = {'message': 'Transaction will be added to Block %s' % index}
        return HttpResponse(json.dumps(response))


class TransactionDetail(APIView):
    def get(self, request):
        return None
