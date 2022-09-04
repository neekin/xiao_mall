from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView, View, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
# Create your views here.
from xiao_shop.models import XiaoShopingCart, XiaoShopCategory
from xiao_shop.conf import xiao_shop_settings
from xiao_shop.utils import add_upload_file
from xiao_shop.forms import XiaoShopLoginForm, XiaoShopRegisterForm

from ..models import RechargeableCard


import random , string ,hashlib


def random_string_generator(str_size=32):
    allowed_chars = string.ascii_letters
    base_str = ''.join(random.choice(allowed_chars) for x in range(str_size))
    return hashlib.md5(base_str.encode('utf-8')).hexdigest()

class BaseView:
    """全局基类视图"""
    
    title = xiao_shop_settings.TITLE
    desc = xiao_shop_settings.DESC
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['desc'] = self.desc
        if self.request.user.is_authenticated:
            context['cart_num'] = XiaoShopingCart.get_cart_count(self.request.user)
        else:
            context['cart_num'] = 0
        return context


class XiaoShopLoginRequiredMixin(LoginRequiredMixin):
    """ 
    全局登陆校验 
    """
    login_url = 'xiao_shop:login'
    redirect_field_name = 'redirect_to'


class XiaoShopLoginView(BaseView, LoginView):
    # i=0
    # money = [50,100,200]
    # random.choice(money)
    # while i<50:
    #     RechargeableCard.objects.create(cardnum=random_string_generator(),num=random.choice(money))
    #     i=i+1
    
    """
    登录视图
    """
    form_class = XiaoShopLoginForm
    template_name = "xiao_shop/login.html"
    next_page = "xiao_shop:index"
    extra_context = {
        "site_title": "登录",
    }


class XiaoShopRegisterView(SuccessMessageMixin, BaseView, FormView):
    """
    注册用户 
    """
    template_name = 'xiao_shop/register.html'
    form_class = XiaoShopRegisterForm
    success_url = reverse_lazy("xiao_shop:index")
    success_message = "%(username)s 注册成功，已登录！"
    
    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            auth_user = authenticate(username=new_user.username, 
                                     password=form.cleaned_data['password1'])
            # UserProfile.objects.create(user=auth_user)
            login(self.request, auth_user)
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=cleaned_data['username'],
        )


class XiaoShopLogoutView(BaseView, LogoutView):
    """
    Log out the user and display the 'You are logged out' message.
    """


class XiaoShopUploadImage(LoginRequiredMixin, View):
    """富文本编辑器上传图片
    首先会检查项目根目录有没有media/upload/的文件夹
    如果没有就创建，图片最终保存在media/upload/目录下
    返回图片路径为 "/media/upload/file.png"
    wangEditor_v4文档：https://www.wangeditor.com/
    """
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        # 无登录后台管理权限的用户不能上传
        if not request.user.is_staff:
            return JsonResponse({"errno": 1,"data":[]})
        
        # 返回数据中需要的data
        data = []
        file_data = request.FILES
        keys = list(file_data.keys())
        for key in keys:
            img_dict = {}
            file = file_data.get(f'{key}')
            # 上传
            add_upload_file(file)
            # 构造返回数据
            img_dict['url'] = f'/{xiao_shop_settings.FILE_PATH}{file.name}'
            data.append(img_dict) 
        context = {"errno": 0,"data":data}
        return JsonResponse(context)


class XiaoShopCategoryAllView(BaseView, TemplateView):
    """ 所有分类
    """
    template_name = 'xiao_shop/categorys.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["navs"] = XiaoShopCategory.get_navs()
        return context