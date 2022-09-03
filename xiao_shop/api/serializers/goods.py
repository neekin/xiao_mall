from rest_framework import serializers

from xiao_shop.models import (
    XiaoShopCategory, XiaoShopBrand, XiaoShopSPU,
    XiaoShopSKU, XiaoShopSpecToOption, XiaoShopSPUSpec, XiaoShopSPUSpecOption,
    XiaoShopSPUCarousel)


class XiaoShopeCategorySerializer(serializers.ModelSerializer):
    """XiaoShopCategory 的序列化器
    """
    sub_cates = serializers.SerializerMethodField()
    brand_cates = serializers.StringRelatedField(many=True)

    class Meta:
        model = XiaoShopCategory
        fields = ('id', 'name', 'desc', 'parent', 'sub_cates', 'brand_cates', 'icon', 'is_nav', 'sort')

    def get_sub_cates(self, obj):
        """序列化自关联子类

        Args:
            obj (当前模型实例): 模型实例对象

        Returns:
            _serializers_: 返回包含子类的序列化器
        """
        if obj.sub_cates:
            return XiaoShopeCategorySerializer(obj.sub_cates, many=True).data
        else:
            return None


class SpuToSkuSerializer(serializers.ModelSerializer):
    """ Spu中所有的SKU 序列化器
    """
    options = serializers.StringRelatedField(many=True)

    class Meta:
        model = XiaoShopSKU
        fields = '__all__'


class XiaoShopSPUSpecOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = XiaoShopSPUSpecOption
        fields = ('id', 'value', 'specs')


class XiaoShopSPUSpecSerializer(serializers.ModelSerializer):
    """XiaoShopSpec 序列化器
    """
    specs = serializers.StringRelatedField(many=True)

    class Meta:
        model = XiaoShopSPUSpec
        fields = ('id', 'name', 'specs')


class XiaoShopSpecToOptionSerializer(serializers.ModelSerializer):
    """XiaoShopSpecToOption 序列化器
    """
    spec = XiaoShopSPUSpecSerializer(many=True)

    class Meta:
        model = XiaoShopSpecToOption
        fields = ['spec']


class XiaoShopSPUCarouselSerializer(serializers.ModelSerializer):
    """XiaoShopSPUCarousel 序列化器
    """
    class Meta:
        model = XiaoShopSPUCarousel
        fields = '__all__'


class XiaoShopSPUSerializer(serializers.ModelSerializer):
    """ SPU 序列化器
    """
    skus = SpuToSkuSerializer(many=True)
    specs = serializers.SerializerMethodField()
    # specs_options = XiaoShopSpecToOptionSerializer(many=True)
    # carousel = XiaoShopSPUCarouselSerializer(many=True)
    carousel = serializers.SerializerMethodField()

    class Meta:
        model = XiaoShopSPU
        fields = '__all__'
    
    def get_specs(self, obj):
        specs = obj.specs_options.filter(is_del=False)
        datas = XiaoShopSpecToOptionSerializer(specs, many=True).data
        specs = []
        if datas:
            ops = datas[0].get('spec')
            for op in ops:
                specs.append(op)
        return specs

    def get_carousel(self, obj):
        carousel = obj.carousel.filter(is_del=False)
        datas = XiaoShopSPUCarouselSerializer(carousel, many=True).data
        datas.insert(0,{
            "img": obj.main_picture.url
        })
        return datas

class XiaoShopSKUSerializer(serializers.ModelSerializer):
    """ SKU 序列化器
    """
    spu = XiaoShopSPUSerializer(many=False)
    options = serializers.StringRelatedField(many=True)

    class Meta:
        model = XiaoShopSKU
        fields = '__all__'


class XiaoShopeCategoryDetailSerializer(serializers.ModelSerializer):

    """XiaoShopCategory 的详情序列化器
    """
    spu_cates = XiaoShopSPUSerializer(many=True)  # 当前分类下的所有spu
    skus = serializers.SerializerMethodField()      # 当前分类下的所有sku

    class Meta:
        model = XiaoShopCategory
        fields = ('id', 'name', 'desc', 'parent', 'sub_cates','skus', 'spu_cates', 'brand_cates', 'icon', 'is_nav', 'sort', )

    def get_skus(self, obj):
        # 返回当前分类下的所有SKU
        spus = obj.spu_cates.filter(is_del=False)
        skus_id = []
        for spu in spus:
            skus_id += list(spu.skus.values_list('id', flat=True))
        queryset = XiaoShopSKU.objects.filter(id__in=skus_id, is_del=False)
        return XiaoShopSKUSerializer(queryset, many=True).data


class XiaoShopBrandSerializer(serializers.ModelSerializer):
    
    """XiaoShopBrand 序列化器
    """
    categories = XiaoShopeCategorySerializer(many=True)
    
    class Meta:
        model = XiaoShopBrand
        fields = ('categories', 'name', 'desc', 'logo', 'sort',)
    

