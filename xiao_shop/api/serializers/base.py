from rest_framework import serializers
from xiao_shop.models import XiaoShopBanner


class XiaoShopBannerSerializer(serializers.ModelSerializer):
    """
    Banner Serializer
    """
    class Meta:
        model = XiaoShopBanner
        fields = "__all__"