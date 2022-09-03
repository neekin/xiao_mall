from rest_framework.pagination import PageNumberPagination
from xiao_shop.conf import xiao_shop_settings


class XiaoShopSKUPagination(PageNumberPagination):
    """ 商品分页 """
    page_size = xiao_shop_settings.PAGE_SIZE
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = xiao_shop_settings.MAX_PAGE_SIZE
    