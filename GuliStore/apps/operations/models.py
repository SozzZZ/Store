from django.db import models
from datetime import datetime
from users.models import UserProfile
from goods.models import GoodsInfo
# Create your models here.
class UserFav(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='所属用户')
    goods = models.ForeignKey(GoodsInfo, verbose_name='所属商品')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.goods.username

    class Meta:
        verbose_name = '用户收藏信息'
        verbose_name_plural = verbose_name

class UserMessage(models.Model):
    MSG_TYPE = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购"),
    )
    user = models.ForeignKey(UserProfile, verbose_name='所属用户')
    mes_type = models.IntegerField(default=1, choices=MSG_TYPE, verbose_name='留言类型')
    subject = models.CharField(max_length=50, verbose_name='留言主题')
    message = models.CharField(max_length=300, verbose_name='留言内容')
    file = models.FileField(upload_to='users/files', verbose_name='留言文件')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = '用户留言信息'
        verbose_name_plural = verbose_name

class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='所属用户')
    province = models.CharField(max_length=50, verbose_name='省')
    city = models.CharField(max_length=50, verbose_name='市')
    district = models.CharField(max_length=50, verbose_name='区')
    signing_name = models.CharField(max_length=20, verbose_name='收货人')
    address = models.CharField(max_length=100, verbose_name='详细地址')
    signing_mobile= models.CharField(max_length=11, verbose_name='收货号码')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.signing_name

    class Meta:
        verbose_name = '用户收货地址信息'
        verbose_name_plural = verbose_name
