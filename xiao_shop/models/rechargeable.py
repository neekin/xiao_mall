from django.db import models
from .models import BaseModelMixin


class RechargeableCard(BaseModelMixin):
    cardnum = models.CharField(
        blank=True, default="",
        unique=True, max_length=32,
        verbose_name="充值卡号", help_text="充值卡号")
    num = models.DecimalField(verbose_name="金额",max_digits=9,decimal_places=2)
    is_use = models.BooleanField(default=False,verbose_name='是否使用了')
    class Meta:
        verbose_name = '充值卡'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.cardnum
