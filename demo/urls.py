from demo import views
from django.urls import path
from demo.views import Block, Node, Transaction, Consensus


urlpatterns = [
    path('transactions/', Transaction.TransactionList.as_view()),
    path('transactions/<pk>/', Transaction.TransactionDetail.as_view()),
    path('blocks/', Block.BlockList.as_view()),
    path('clocks/<pk>/', Block.BlockDetail.as_view()),
    path('nodes/', Node.NodeList.as_view()),
    path('resolve/', Consensus.Consensus.as_view()),
]