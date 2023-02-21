from datetime import date
from typing import Any

from _decimal import Decimal
from dateutil.relativedelta import relativedelta
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from deposits.models import DepositProducts, Deposits
from deposits.serializers import (
    DepositProductSerializer,
    DepositProductsListSerializer,
    DepositSerializer,
    DepositsListSerializer,
)
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from deposits.utils import IsAdminOrReadOnly


class DepositProductsListView(generics.ListCreateAPIView):
    queryset = DepositProducts.objects.all()
    serializer_class = DepositProductsListSerializer
    permission_classes = (IsAdminOrReadOnly, )


class DepositProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepositProducts.objects.all()
    serializer_class = DepositProductSerializer
    permission_classes = (IsAdminOrReadOnly, )


class DepositsListView(generics.ListCreateAPIView):
    queryset = Deposits.objects.all()
    serializer_class = DepositsListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def create(self: "DepositCreateView", request: Request, *args: Any, **kwargs: Any) -> Response:
        product = DepositProducts.objects.get(pk=request.data["deposit_product_id"])

        if Decimal(request.data["amount"]) > product.max_amount or Decimal(request.data["amount"]) < product.min_amount:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Wrong deposit amount")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, product)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @staticmethod
    def perform_create(serializer: DepositSerializer, product: DepositProducts) -> None:
        ends_at = date.today()

        instance = serializer.save(ends_at=ends_at)

        created_at = instance.created_at
        ends_at = created_at + relativedelta(months=product.duration)

        serializer.save(ends_at=ends_at)


class DepositView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposits.objects.all()
    serializer_class = DepositSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
