from demo import views
from django.urls import path
from demo.views import block, node, transaction, consensus


urlpatterns = [
    path('transactions/', transaction.TransactionList.as_view()),
    path('transactions/<pk>/', transaction.TransactionDetail.as_view()),
    path('blocks/', block.BlockList.as_view()),
    path('blocks/<pk>/', block.BlockDetail.as_view()),
    path('nodes/', node.NodeList.as_view()),
    path('resolve/', consensus.Consensus.as_view()),
]