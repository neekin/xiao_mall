from rest_framework import serializers
from ...models import XiaoShopRate, XiaoShopOrderSKU


class XiaoShopRateSerializer(serializers.ModelSerializer):
    """
    XiaoShopRate Serializer
    """
    owner = serializers.HiddenField(
        default = serializers.CurrentUserDefault())
    
    class Meta:
        model = XiaoShopRate
        # fields = "__all__"
        exclude = ("content_type", )