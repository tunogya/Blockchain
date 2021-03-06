from demo.models.event import Event
from rest_framework import mixins
from rest_framework import generics
from demo.serializers import EventSerializer


# 节点列表
class NodeList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):

    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filterset_fields = ['id', 'name', 'type']

    # 返回所有节点
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # 注册节点
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NodeDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
