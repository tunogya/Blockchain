from uuid import uuid4
from rest_framework.views import APIView

from demo.utils.Blockchain import Blockchain

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


# 节点列表
class NodeList(APIView):
    # 返回所有节点
    def get(self, request):
        return None

    # 注册节点
    def post(self, request):
        return None

