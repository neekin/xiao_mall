from unicodedata import name
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.goods import (
    XiaoShopCategoryViewsets, XiaoShopBrandViewsets, XiaoShopSPUViewsets,
    XiaoShopSKUViewsets)

from .views.order import (
    XiaoShopingCartViewsets, XiaoShopAddressViewsets, XiaoShopOrderInfoViewSet, XiaoShopPayViewSet)

from .views.base import XiaoShopBannerViewsets
from .views.comment import XiaoShopRateViewsets

router = DefaultRouter()

# 分类接口
## list        /categories/
## retrieve    /categories/{id}/
router.register('categories', XiaoShopCategoryViewsets, basename="categories")

# 品牌接口
router.register('brands', XiaoShopBrandViewsets, basename="brands")

# 商品详情接口
router.register('spu_goods', XiaoShopSPUViewsets, basename="spu_goods")

# 商品详情接口
router.register('sku_goods', XiaoShopSKUViewsets, basename="sku_goods")

# 购物车接口，增删改查
router.register('carts', XiaoShopingCartViewsets, basename="carts")

# 收货地址接口
router.register('address', XiaoShopAddressViewsets, basename="address")

# 订单接口
router.register('orderinfo', XiaoShopOrderInfoViewSet, basename="orderinfo")

# banner接口
router.register('banners', XiaoShopBannerViewsets, basename="banners")

# 商品列表页立即支付接口
router.register('paynow', XiaoShopPayViewSet, basename="paynow")

# 商品打分接口
router.register('rate', XiaoShopRateViewsets, basename="rate")


urlpatterns = router.urls
