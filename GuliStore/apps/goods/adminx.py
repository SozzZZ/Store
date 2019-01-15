from .models import *
import xadmin
from xadmin import views

class GoodsCategoryAdmin(object):
    list_display = ['name', 'category_type', 'code', 'parent_category', 'is_tab', 'add_time']
    model_icon = 'fa fa-rocket'

class GoodsInfoAdmin(object):
    list_display = ['category', 'name',  'goods_sn', 'click_num', 'fav_num', 'add_time']
    style_fields = {'desc':'ueditor'}

class CategoryBrandAdmin(object):
    list_display = ['category', 'name', 'image', 'add_time']

class GoodsImageAdmin(object):
    list_display = ['goods', 'image', 'add_time']

class BannerAdmin(object):
    list_display = ['goods', 'image', 'index','add_time']

class StudentAdmin(object):
    list_display = ['name', 'age', 'add_time']

class CommXadminSetting():
    site_title = '谷粒商城后台管理系统'
    site_footer = 'SozzZZ'
    menu_style = 'accordion'

class BaseXadminSetting():
    enable_themes = True
    use_bootswatch = True



xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsInfo, GoodsInfoAdmin)
xadmin.site.register(CategoryBrand, CategoryBrandAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.CommAdminView, CommXadminSetting)
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
xadmin.site.register(Student, StudentAdmin)
