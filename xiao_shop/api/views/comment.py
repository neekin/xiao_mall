from xml.dom import VALIDATION_ERR
from django.forms import ValidationError
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from xiao_shop.api.permissions import IsOwnerOrReadOnly
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status
from ...models import XiaoShopRate, XiaoShopOrderSKU, XiaoShopOrderInfo
from ..serializers.comment import XiaoShopRateSerializer


class XiaoShopRateViewsets(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """XiaoShopRate视图
    list:
        XiaoShopRate列表
    create:
        post打分接口
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = XiaoShopRate.objects.all()
    serializer_class = XiaoShopRateSerializer
    authentication_classes = [SessionAuthentication]
      
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        object_id = serializer.validated_data['object_id']
        
        order_sku = XiaoShopOrderSKU.objects.filter(order__owner=self.request.user, id=object_id)
        # 判断是否已经评价过，不可重复评价
        if order_sku.exists() and order_sku.first().is_commented:
            return Response({'error':'该商品已经评价！'}, status=status.HTTP_403_FORBIDDEN)
        # 判断订单状态是否已确认收货，确认收货后才可以评价！
        elif order_sku.exists() and not order_sku.first().is_commented and order_sku.first().order.pay_status==4:
            # 要评价的模型content_type
            content_type = ContentType.objects.get_for_model(XiaoShopOrderSKU)
            serializer.validated_data['content_type'] = content_type
            # 保存评价
            self.perform_create(serializer)
            # 标记为已评价
            order_sku.update(is_commented=True)
            # 如果该订单中的商品全部已评价，则修改该订单状态为已完成
            order = order_sku.first().order
            is_commented = XiaoShopOrderSKU.objects.filter(order__owner=request.user, order=order).values_list('is_commented', flat=True)
            if all(list(is_commented)):
                order.pay_status = 5
                order.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'error':'商品不存在或该订单未确认收获！'}, status=status.HTTP_404_NOT_FOUND)
    