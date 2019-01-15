import os,sys
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
sys.path.append(dir_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GuliStore.settings")
import django
django.setup()

from goods.models import GoodsCategory
from db_tools.data.category_data import row_data

for item1 in row_data:
    cat1 = GoodsCategory()
    cat1.name = item1['name']
    cat1.code = item1['code'] if item1['code'] else ''
    cat1.category_type = 1
    cat1.save()
    for item2 in item1['sub_categorys']:
        cat2 = GoodsCategory()
        cat2.name = item2['name']
        cat2.code = item2['code'] if item2['code'] else ''
        cat2.category_type = 2
        cat2.parent_category = cat1
        cat2.save()
        for item3 in item2['sub_categorys']:
            cat3 = GoodsCategory()
            cat3.name = item3['name']
            cat3.code = item3['code'] if item3['code'] else ''
            cat3.category_type = 3
            cat3.parent_category = cat2
            cat3.save()