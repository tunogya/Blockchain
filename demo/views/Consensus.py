from rest_framework.views import APIView


class Consensus(APIView):
    # 解决冲突
    def get(self, request):
        return None