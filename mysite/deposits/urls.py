from deposits.views import (
    DepositProductsListView,
    DepositProductView,
    DepositsListView,
    DepositView,
)
from django.urls import path, include

urlpatterns = [
    path("deposit-products/", DepositProductsListView.as_view()),
    path("deposit-products/<int:pk>/", DepositProductView.as_view()),
    path("deposits/", DepositsListView.as_view()),
    path("deposits/<int:pk>/", DepositView.as_view()),
]
