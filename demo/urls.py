from demo import views
from django.urls import path
from demo.views import Chain, Node, Transaction, Consensus


urlpatterns = [
    path('transactions/', Transaction.TransactionList.as_view()),
    path('transactions/<pk>/', Transaction.TransactionDetail.as_view()),
    path('chains/', Chain.ChainList.as_view()),
    path('chains/<pk>/', Chain.ChainDetail.as_view()),
    path('nodes/', Node.NodeList.as_view()),
    path('resolve/', Consensus.Consensus.as_view()),
]