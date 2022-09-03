from django.views.generic import TemplateView, DetailView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
# from django.conf import settings
from xiao_shop.conf import xiao_shop_settings
from xiao_shop.models import (
    XiaoShopCategory, XiaoShopSPU, XiaoShopBrand, XiaoShopSKU,
    XiaoShopRate, XiaoShopOrderSKU)
from xiao_shop.filters import XiaoShopSPUFilter, XiaoShopSKUFilter
from xiao_shop.models.order import XiaoShopOrderInfo

from .views import BaseView


class IndexView(BaseView, TemplateView):
    """首页视图"""
    template_name = 'xiao_shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cate_skus_dict'] = self.get_cate_skus()
        return context
    
    def get_cate_skus(self):
        parent_cates = XiaoShopCategory.objects.filter(parent__isnull=True, is_nav=True)
        cate_skus_dict = {}
        for cate in parent_cates:
            sub_cates = cate.sub_cates.filter(is_del=False, is_nav=True).values_list('id', flat=True)
            skus = XiaoShopSKU.objects.filter(spu__category__id__in=list(sub_cates)).distinct()
            print(skus)
            cate_skus_dict[cate.name] = skus[:xiao_shop_settings.FLOOR_NUM]
        return cate_skus_dict


class XiaoShopCategoryView(BaseView, SingleObjectMixin, ListView):
    """ 商品列表页即商品分类详情页
    最终返回的是当前分类下的sku的queryset数据
    """
    template_name = "xiao_shop/goods.html"
    paginate_by = xiao_shop_settings.PAGE_SIZE
    
    def get(self, request, *args, **kwargs):
        # 当前分类数据
        self.object = self.get_object(queryset=XiaoShopCategory.objects.filter(is_del=False))
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        qs_filter = self.get_filter_queryset()
        queryset = qs_filter.qs
        return queryset
    
    def get_filter_queryset(self):
        """ 筛选过的数据 """
        spus = self.object.spu_cates.filter(is_del=False)
        skus_id = []
        for spu in spus:
            skus_id += list(spu.skus.values_list('id', flat=True))
        queryset = XiaoShopSKU.objects.filter(id__in=skus_id, is_del=False)
        return XiaoShopSKUFilter(self.request.GET, queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goods'] = self.get_filter_queryset()
        context['brands'] = self.get_brands()
        context['category'] = self.object

        if self.request.GET.get('brand'):
            context['brand_id'] = int(self.request.GET.get('brand'))
        else:
            context['brand_id'] = None
        return context
    
    def get_brands(self):
        """ 当前分类的品牌数据 """
        return self.object.brand_cates.filter(is_del=False)


class XiaoShopSPUDetailView(BaseView, DetailView):
    """ 商品详情页
    """
    queryset = XiaoShopSPU.objects.filter(is_del=False)
    template_name = 'xiao_shop/detail.html'
    context_object_name = 'spu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goods_news'] = self.get_goods()[:xiao_shop_settings.NEW_NUM]
        context['comments'] = self.get_rates_all()
        context['rate'] = self.get_rate() 
        context['score'] = self.get_score()
        return context

    def get_goods(self):
        # 新品推荐
        cates = self.get_object().category.filter(is_del=False)
        skus_id = []
        for cate in cates:
            spus = cate.spu_cates.filter(is_del=False, is_new=True)
            for spu in spus:
                skus_id += list(spu.skus.values_list('id', flat=True))
        queryset = XiaoShopSKU.objects.filter(id__in=list(set(skus_id)), is_del=False)
        if not queryset:
            queryset = self.get_object().skus.filter(is_del=False)
        return queryset
    
    def get_rates_all(self):
        """当前商品下的所有评价
        """
        # 当前spu下的所有sku
        skus_ids = self.get_object().skus.values_list('id', flat=True)
        # 拥有评论的sku_ids
        object_ids = XiaoShopRate.objects.values_list('object_id', flat=True)
        # 当前商品下拥有的评论
        rates_list = []
        for object_id in object_ids:
            if XiaoShopOrderSKU.objects.get(id=object_id).sku.id in skus_ids:
                rates_list.append(XiaoShopRate.objects.get(object_id=object_id))  
        return rates_list
    
    def get_rate_gt_2(self):
        # 评分大于2的评价列表
        rates = []
        for rate in self.get_rates_all():
            if rate.rate >2:
                rates.append(rate)
        return rates
    
    def get_rate(self):
        """当前商品的评分
        计算方式为：求平均分
        如果还未有评价，则默认评分为4.6分
        """
        try:
            rate = sum([rate.rate for rate in self.get_rates_all()]) / len(self.get_rates_all())
        except ZeroDivisionError:
            rate = 4.6
        return rate
    
    def get_score(self):
        """评价满意度
        算法：评分大于2的数量在总评价数中的占比
        无评论默认为98%
        """
        try:
            score = f'{len(self.get_rate_gt_2()) / len(self.get_rates_all()) * 100}%'
        except ZeroDivisionError:
            score = '98%'
        return score