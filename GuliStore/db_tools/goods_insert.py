import os,sys
#找到当前目录的路径 , 将其加入到django的搜索环境中
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
sys.path.append(dir_path)
#加载django的环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GuliStore.settings")
#初始化加载好的环境
import django
django.setup()

from goods.models import GoodsInfo, GoodsCategory, GoodsImage
from db_tools.data.product_data import row_data

for item in row_data:
    goods = GoodsInfo()
    goods.name = item['name']
    goods.goods_brief = item['desc'] if item['desc'] else ''
    goods.desc = item['goods_desc'] if item['goods_desc'] else ''
    goods.market_price = float(item['market_price'].replace('￥','').replace('元',''))
    goods.shop_price = float(item['sale_price'].replace('￥','').replace('元',''))
    goods.goods_front_image = item['images'][0] if item['images'] else ''

    category_list = GoodsCategory.objects.filter(name = item['categorys'][-1])
    if category_list:
        goods.category = category_list[0]
    goods.save()

    for image in item['images']:
        goods_image = GoodsImage()
        goods_image.goods = goods
        goods_image.image = image
        goods_image.save()
