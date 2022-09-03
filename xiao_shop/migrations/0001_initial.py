# Generated by Django 4.0.3 on 2022-03-31 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='XiaoShopBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('img', models.ImageField(max_length=200, upload_to='XiaoShop/carousel/', verbose_name='轮播图')),
                ('img_url', models.CharField(blank=True, default='', max_length=50, verbose_name='外链图片')),
                ('target_url', models.URLField(blank=True, default='', verbose_name='跳转链接')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='XiaoShopBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='品牌名称')),
                ('desc', models.CharField(blank=True, default='', max_length=100, verbose_name='品牌描述')),
                ('logo', models.ImageField(blank=True, max_length=200, null=True, upload_to='XiaoShop/brand/', verbose_name='品牌logo')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '商品品牌',
                'verbose_name_plural': '商品品牌',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='XiaoShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('desc', models.CharField(blank=True, default='', max_length=100, verbose_name='分类描述')),
                ('icon', models.ImageField(blank=True, help_text='大小为 96px * 96px', max_length=200, null=True, upload_to='XiaoShop/cateicon/', verbose_name='分类图标')),
                ('is_nav', models.BooleanField(default=False, verbose_name='是否为导航')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cates', to='xiao_shop.xiaoshopcategory', verbose_name='父级分类')),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='XiaoShopOrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('order_sn', models.CharField(blank=True, default='', help_text='订单号', max_length=32, unique=True, verbose_name='订单号')),
                ('trade_sn', models.CharField(blank=True, help_text='交易号', max_length=64, null=True, unique=True, verbose_name='交易号')),
                ('pay_status', models.IntegerField(choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成'), (6, '已取消')], default=1, help_text='支付状态', verbose_name='支付状态')),
                ('pay_method', models.IntegerField(choices=[(1, '货到付款'), (2, '支付宝'), (3, '微信支付'), (4, '余额支付')], default=2, help_text='支付方式', verbose_name='支付方式')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品总金额')),
                ('order_mark', models.CharField(blank=True, default='', help_text='订单备注', max_length=100, verbose_name='订单备注')),
                ('freight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='运费')),
                ('name', models.CharField(default='', max_length=50, verbose_name='签收人')),
                ('phone', models.CharField(default='', max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, default='', max_length=50, verbose_name='邮箱')),
                ('address', models.CharField(max_length=150, verbose_name='地址')),
                ('pay_time', models.DateTimeField(blank=True, help_text='支付时间', null=True, verbose_name='支付时间')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
        migrations.CreateModel(
            name='XiaoShopSPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=60, verbose_name='商品标题')),
                ('sub_title', models.CharField(max_length=100, verbose_name='商品副标题')),
                ('desc', models.CharField(blank=True, max_length=150, null=True, verbose_name='商品简介')),
                ('main_picture', models.ImageField(max_length=200, upload_to='XiaoShop/spu/', verbose_name='商品主图')),
                ('stocks', models.PositiveIntegerField(default=0, verbose_name='总库存')),
                ('sales', models.PositiveIntegerField(default=0, verbose_name='总销量')),
                ('content', models.TextField(verbose_name='商品详情')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热销')),
                ('is_best', models.BooleanField(default=False, verbose_name='是否精品')),
                ('is_shelves', models.BooleanField(default=False, verbose_name='是否促销')),
                ('after_services', models.TextField(blank=True, default='', verbose_name='售后说明')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xiao_shop.xiaoshopbrand', verbose_name='商品品牌')),
                ('category', models.ManyToManyField(related_name='spu_cates', to='xiao_shop.xiaoshopcategory', verbose_name='商品分类')),
            ],
            options={
                'verbose_name': '商品SPU',
                'verbose_name_plural': '商品SPU',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='XiaoShopSPUSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='规格名称')),
            ],
            options={
                'verbose_name': '商品规格',
                'verbose_name_plural': '商品规格',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='XiaoShopSPUSpecOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('value', models.CharField(max_length=50, verbose_name='规格值')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specs', to='xiao_shop.xiaoshopspuspec', verbose_name='规格')),
            ],
            options={
                'verbose_name': '商品规格值',
                'verbose_name_plural': '商品规格值',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='XiaoShopSPUCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('img', models.ImageField(max_length=200, upload_to='XiaoShop/carousel/', verbose_name='轮播图')),
                ('img_url', models.CharField(blank=True, default='', max_length=50, verbose_name='外链图片')),
                ('target_url', models.URLField(blank=True, default='', verbose_name='跳转链接')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='xiao_shop.xiaoshopspu', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品轮播图',
                'verbose_name_plural': '商品轮播图',
            },
        ),
        migrations.CreateModel(
            name='XiaoShopSpecToOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('spec', models.ManyToManyField(to='xiao_shop.xiaoshopspuspec', verbose_name='规格')),
                ('spu', models.ManyToManyField(blank=True, related_name='specs_options', to='xiao_shop.xiaoshopspu', verbose_name='商品SPUS')),
            ],
            options={
                'verbose_name': '商品规格关系',
                'verbose_name_plural': '商品规格关系',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='XiaoShopSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('main_picture', models.ImageField(max_length=200, upload_to='XiaoShop/sku/', verbose_name='商品主图')),
                ('bar_code', models.CharField(blank=True, default='', max_length=50, verbose_name='商品条码')),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品售价')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='市场价/划线价')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='成本价')),
                ('stocks', models.PositiveIntegerField(default=0, verbose_name='库存')),
                ('sales', models.PositiveIntegerField(default=0, verbose_name='销量')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
                ('options', models.ManyToManyField(blank=True, to='xiao_shop.xiaoshopspuspecoption', verbose_name='规格值')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skus', to='xiao_shop.xiaoshopspu', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品SKU',
                'verbose_name_plural': '商品SKU',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='XiaoShopOrderSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='单价')),
                ('is_commented', models.BooleanField(default=False, verbose_name='是否已评价')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='xiao_shop.xiaoshoporderinfo', verbose_name='订单')),
                ('sku', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='xiao_shop.xiaoshopsku', verbose_name='订单商品')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
            },
        ),
        migrations.CreateModel(
            name='XiaoShopingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('num', models.PositiveIntegerField(default=1, verbose_name='数量')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xiao_shop.xiaoshopsku', verbose_name='商品sku')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.AddField(
            model_name='xiaoshopbrand',
            name='categories',
            field=models.ManyToManyField(blank=True, help_text='多对多', related_name='brand_cates', to='xiao_shop.xiaoshopcategory', verbose_name='所属分类'),
        ),
        migrations.CreateModel(
            name='XiaoShopAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='签收人')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, default='', max_length=50, verbose_name='邮箱')),
                ('province', models.CharField(max_length=150, verbose_name='省')),
                ('city', models.CharField(max_length=150, verbose_name='市')),
                ('county', models.CharField(max_length=150, verbose_name='区/县')),
                ('address', models.CharField(max_length=150, verbose_name='详细地址')),
                ('is_default', models.BooleanField(default=False, verbose_name='设为默认')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
            },
        ),
        migrations.AddConstraint(
            model_name='xiaoshopingcart',
            constraint=models.UniqueConstraint(fields=('owner', 'sku'), name='unique_owner_sku_happy'),
        ),
        migrations.AddConstraint(
            model_name='xiaoshopaddress',
            constraint=models.UniqueConstraint(fields=('id', 'is_default'), name='unique_happy_addr'),
        ),
    ]