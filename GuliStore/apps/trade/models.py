from django.db import models
from datetime import datetime
from users.models import UserProfile
from goods.models import GoodsInfo
# Create your models here.
class ShoppingCart(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='所属用户')
    goods = models.ForeignKey(GoodsInfo, verbose_name='所属商品')
    nums = models.IntegerField(default=1 , verbose_name='购买数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.goods.name

    class Meta:
        verbose_name = '购物车信息'
        verbose_name_plural = verbose_name

class OrderInfo(models.Model):
    ORDER_STATUS = (
        ("PAYING", "待支付"),
        ("TRADE_SUCESS", "支付成功"),
        ("TRADE_CLOSE", "支付关闭"),
        ("TRADE_FAIL", "支付失败"),
        ("TRADE_FINSHED", "交易结束"),
    )
    user = models.ForeignKey(UserProfile, verbose_name='所属用户')
    order_sn = models.CharField(max_length=30, verbose_name='订单编号', unique=True)
    order_mount = models.FloatField(verbose_name='订单总额')
    order_message = models.CharField(max_length=300, verbose_name='订单留言', null=True, blank=True)

    trade_id =models.CharField(max_length=50, verbose_name='交易流水号', unique=True, null=True, blank=True)
    trade_status = models.CharField(max_length=20 ,choices=ORDER_STATUS, verbose_name='订单状态', default='PAYING')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')

    signing_name = models.CharField(max_length=50, verbose_name='收货人')
    signing_phone = models.CharField(max_length=11, verbose_name='收货手机')
    signing_address = models.CharField(max_length=200, verbose_name='收货地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.order_sn

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

class OrderGoods(models.Model):
    goods = models.ForeignKey(GoodsInfo, verbose_name='所属商品')
    order = models.ForeignKey(OrderInfo, verbose_name='所属订单')
    nums = models.IntegerField(default=1, verbose_name='商品数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.order.order_sn

    class Meta:
        verbose_name = '订单商品信息'
        verbose_name_plural = verbose_name


