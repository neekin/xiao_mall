from rest_framework import viewsets
from rest_framework import mixins
from xiao_shop.models import XiaoShopBanner
from xiao_shop.api.serializers.base import XiaoShopBannerSerializer


class XiaoShopBannerViewsets(mixins.ListModelMixin, viewsets.GenericViewSet):
    """banner视图
    list:
        banner列表
    """
    serializer_class = XiaoShopBannerSerializer

    def get_queryset(self):
        return XiaoShopBanner.objects.filter(is_del=False)