from deposits.models import DepositProducts, Deposits
from rest_framework import serializers


class DepositProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = "__all__"


class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = "__all__"


class DepositsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposits
        fields = "__all__"


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposits
        fields = "__all__"
