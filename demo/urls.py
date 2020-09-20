from demo import views
from django.urls import path


urlpatterns = [
    path('mine/', views.mine),
    path('transactions/new/', views.new_transaction),
    path('chain/', views.full_chain),
    path('register/', views.register_nodes),
    path('resolve/', views.consensus),
]