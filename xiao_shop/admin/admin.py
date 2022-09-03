from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy
from django.urls import reverse_lazy
from xiao_shop.conf import xiao_shop_settings
from .forms import XiaoShopAdminAuthenticationForm


class XiaoShopAdminSite(AdminSite):
    """自定义AdminSite
    """
    site_header = gettext_lazy("XiaoShopAdmin")
    site_title = gettext_lazy("Happyshop后台管理")
    index_title = gettext_lazy("Site administration")
    site_url = reverse_lazy("xiao_shop:index")
    
    # index_template = "xiao_shop/admin/index.html"
    
    login_form = XiaoShopAdminAuthenticationForm
    login_template = "xiao_shop/admin/login.html"
     
    def login(self, request, extra_context=None):
        extra_context = {
            'title': xiao_shop_settings.TITLE,
            'desc': xiao_shop_settings.DESC,
            'logo': xiao_shop_settings.LOGO
        }
        return super().login(request, extra_context)
    
    def index(self, request, extra_context=None):
        extra_context = {
            'num':'num'
        }
        print(extra_context)
        return super().index(request, extra_context)
    
    
xiao_shop_site = XiaoShopAdminSite(name='xiao_shop_admin')
