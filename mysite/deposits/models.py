import uuid

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
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
    interest_rate = DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(limit_value=0)])
    duration = IntegerField()  # DurationField()
    min_amount = DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(limit_value=0)])
    max_amount = DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(limit_value=0)])
    is_debit_allowed = BooleanField()
    is_credit_allowed = BooleanField()
    capitalization = BooleanField()
    premature_termination = BooleanField()

    def clean(self):
        if self.min_amount >= self.max_amount:
            raise ValidationError("Min amount should be less than Max amount")

    def __str__(self: "DepositProducts") -> CharField:
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(currency__in=[cur.code for cur in Currency]),
                name='valid_currency_depositProducts'
            )
        ]


class Deposits(models.Model):
    user_uuid = UUIDField(default=uuid.uuid4)
    account_number = CharField(max_length=34)
    interest_account_id = IntegerField()
    amount = DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(limit_value=0)])
    deposit_product = ForeignKey(DepositProducts, on_delete=PROTECT)
    auto_prolongation = BooleanField()
    created_at = DateField(auto_now_add=True)
    ends_at = DateField(editable=False)
    updated_at = DateField(auto_now=True)
    status = CharField(max_length=6, choices=[("ACTIVE", "ACTIVE"), ("CLOSED", "CLOSED")])

    def clean(self):
        if self.deposit_product.min_amount >= self.amount >= self.deposit_product.max_amount:
            raise ValidationError("Amount should be less than max amount and greater than min amount of debit product")

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(status__in=["ACTIVE", "CLOSED"]),
                name='valid_status_deposits'
            )
        ]
