from rest_framework import mixins
from rest_framework import generics
from demo.serializers import TransactionSerializer
from demo.models.Transaction import Transaction


# 交易
class TransactionList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filterset_fields = ['id', 'state']

    # 返回所有交易
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # 创建一个交易
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TransactionDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
