from rest_framework import viewsets

from accounts.models import Accounts, Transactions
from accounts.serializers import AccountsSerializer, TransactionsSerializer


class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
