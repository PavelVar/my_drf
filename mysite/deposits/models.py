import uuid

from django.db import models
from django.db.models import (
    PROTECT,
    BooleanField,
    CharField,
    DateField,
    DecimalField,
    ForeignKey,
    IntegerField,
    UUIDField,
)
from iso4217 import Currency


class DepositProducts(models.Model):
    name = CharField(max_length=255, unique=True)
    currency = CharField(max_length=5, choices=[(cur.code, cur.code) for cur in Currency])
    interest_rate = DecimalField(max_digits=10, decimal_places=2)
    duration = IntegerField()  # DurationField()
    min_amount = DecimalField(max_digits=20, decimal_places=2)
    max_amount = DecimalField(max_digits=20, decimal_places=2)
    is_debit_allowed = BooleanField()
    is_credit_allowed = BooleanField()
    capitalization = BooleanField()
    premature_termination = BooleanField()

    def __str__(self: "DepositProducts") -> CharField:
        return self.name


class Deposits(models.Model):
    user_uuid = UUIDField(default=uuid.uuid4)
    account_number = CharField(max_length=34)
    interest_account_id = IntegerField()
    amount = DecimalField(max_digits=20, decimal_places=2)
    deposit_product_id = ForeignKey(DepositProducts, on_delete=PROTECT)
    auto_prolongation = BooleanField()
    created_at = DateField(auto_now_add=True)
    ends_at = DateField(editable=False)
    updated_at = DateField(auto_now=True)
    status = CharField(max_length=6, choices=[("A", "ACTIVE"), ("C", "CLOSED")])
