from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from .import views

app_name = "xiao_shop"

urlpatterns = [
    path('api/', include('xiao_shop.api.api_urls')),
    path('docs/', include_docs_urls(title='XiaoShop API')),
    path('api-auth/', include('rest_framework.urls')),
    
    # PC端
    path("", views.IndexView.as_view(), name="index"),
    path("all_category/", views.XiaoShopCategoryAllView.as_view(), name="all_category"),
    path("goods/<int:pk>/", views.XiaoShopCategoryView.as_view(), name="goods"),
    path("goods/<int:pk>/detail/", views.XiaoShopSPUDetailView.as_view(), name="goods_detail"),
    path("cart/", views.XiaoShopingCartView.as_view(), name="cart"),
    path("pay/", views.XiaoShopPayView.as_view(), name="pay"),
    path('user_profile/', views.XiaoShopUserProfileView.as_view(), name='user_profile'),
    path('user_orders/', views.XiaoShopUserOrdersView.as_view(), name='user_orders'),
    path('user_orders/<int:pk>/', views.XiaoShopUserOrdersDetailView.as_view(), name='user_orders_detail'),
    path('user_address/', views.XiaoShopUserAddressView.as_view(), name='user_address'),
    path("user_orders_sku/<int:pk>/", views.XiaoShopOrderSKUDetailView.as_view(), name="user_orders_sku_detail"),
    
    
    path("login/", views.XiaoShopLoginView.as_view(), name="login"),
    path("register/", views.XiaoShopRegisterView.as_view(), name="register"),
    path('logout/', views.XiaoShopLogoutView.as_view(), name='logout'),
    path('upload_img/', views.XiaoShopUploadImage.as_view(), name="upload_img"),
]