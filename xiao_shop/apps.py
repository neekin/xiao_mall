from django.apps import AppConfig


class XiaoShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'xiao_shop'

    def ready(self) -> None:
        from . import signals