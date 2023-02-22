import uuid

from django.db import models
from django.db.models import UUIDField, CharField, DecimalField, DateField, ForeignKey, PROTECT, IntegerField, TextField
from django.utils.translation import gettext_lazy as _
from iso4217 import Currency

from accounts.utils import generate_account_number


class Accounts(models.Model):
    class AccountType(models.TextChoices):
        CREDIT = "CREDIT", _('Credit')
        CURRENT = "CURRENT", _('Current')
        DEPOSIT = "DEPOSIT", _('Deposit')
        INTEREST = "INTEREST", _('Interest')

    user_uuid = UUIDField(default=uuid.uuid4)
    account_number = CharField(max_length=25, unique=True, editable=False, default=generate_account_number)
    currency = CharField(max_length=5, choices=[(cur.code, cur.code) for cur in Currency])
    amount = DecimalField(max_digits=12, decimal_places=2)
    created_at = DateField(auto_now_add=True)
    account_type = models.CharField(max_length=8, choices=AccountType.choices, default=AccountType.CURRENT)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(currency__in=[cur.code for cur in Currency]),
                name='valid_currency_accounts'
            )
        ]


class Transactions(models.Model):
    class TransactionsCategoriesEnum(models.TextChoices):
        WITHDRAWAL = "WITHDRAWAL"
        PAYMENT = "PAYMENT"
        INTERNAL_TRANSFER = "INTERNAL_TRANSFER"
        COMISSION = "COMISSION"
        PAYMENT_FOR_BANK_SERVICES = "PAYMENT_FOR_BANK_SERVICES"

    account_from = ForeignKey(Accounts, on_delete=PROTECT, related_name='transactions_from')
    account_to = ForeignKey(Accounts, on_delete=PROTECT, related_name='transactions_to')
    amount = DecimalField(max_digits=12, decimal_places=2)
    currency = CharField(max_length=5, choices=[(cur.code, cur.code) for cur in Currency])
    card_id = IntegerField(null=True)
    category = models.CharField(max_length=30, choices=TransactionsCategoriesEnum.choices, default=TransactionsCategoriesEnum.PAYMENT)
    comment = TextField()
    created_at = DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(currency__in=[cur.code for cur in Currency]),
                name='valid_currency_transaction'
            )
        ]
