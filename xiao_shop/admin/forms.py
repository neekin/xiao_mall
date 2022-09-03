from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _

from ..forms import XiaoShopTextInput, XiaoShopPasswordInput


class XiaoShopAdminAuthenticationForm(AdminAuthenticationForm):
    """后台登录表单
    """
    username = UsernameField(widget=XiaoShopTextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=XiaoShopPasswordInput(attrs={"autocomplete": "current-password"}),
    )