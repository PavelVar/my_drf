from django.urls import path

from accounts.views import AccountsViewSet, TransactionsViewSet

urlpatterns = [
    path("accounts/", AccountsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("accounts/<int:pk>/", AccountsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'})),
    path("transactions/", TransactionsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("transactions/<int:pk>/", TransactionsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'})),
]
