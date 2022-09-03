from django_filters import rest_framework as filters
from xiao_shop.models import  XiaoShopSKU, XiaoShopSPU, XiaoShopCategory


class XiaoShopSPUFilter(filters.FilterSet):
    """SPU 筛选"""
    order = filters.OrderingFilter(fields=('skus__sell_price',))

    class Meta:
        model = XiaoShopSPU
        fields = ['brand', 'is_new', 'is_hot', 'is_best', 'category', 'is_shelves']


class XiaoShopSKUFilter(filters.FilterSet):
    """ 过滤sku """
    order = filters.OrderingFilter(fields=('sell_price',))

    class Meta:
        model = XiaoShopSKU
        fields = ['spu__brand', 'spu__is_new', 'spu__is_hot', 'spu__is_best', 'spu__is_shelves', 'spu__category']


class XiaoShopCategoryFilter(filters.FilterSet):

    class Meta:
        model = XiaoShopCategory
        fields = ['is_nav', ]
