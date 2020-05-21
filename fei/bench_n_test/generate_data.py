"""生成测试数据
"""
import sys, os

from random import randint
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_settings.settings")
import django
django.setup()

# setup_environ(settings)
import random
from app_models.models import Category, Warehouse, Product

class ProductData(object):
    """生成测试的product

    一个product记录是这个样子的：
            "category": 2,
            "warehouse": 7,
            "product_name": "Gummy Bear VC",
            "product_description": "小熊糖维生素C，150粒",
            "product_price": "150.00",
            "product_stock": 100
    
    测试数据生成过程
        随机选一个category
        随机选一个warehouse
        生成一个product_name
        生成一个product_description
        生成一个product_price
        生成一个product_stock
    """
    def __init__(self):
        # self.category = Category.objects.values("id").order_by("?")[0]
        self._count = row_count
        self._rand_str = str(random.randint(1, 999999))

        self.p = Product()
        self.p.category = Category.objects.all().order_by("?")[0]
        self.p.warehouse = Warehouse.objects.all().order_by("?")[0]
        self.p.product_name = "测试产品_" + self._rand_str
        self.p.product_description = "产品描述_" + self._rand_str
        self.p.product_price = random.uniform(0.01, 100000.00)
        self.p.product_stock = random.randint(0, 9999)


# p = ProductData()
# print(p.category)
if __name__ == '__main__':

    print(f'Current Product count BEFORE: {Product.objects.count()}')
    row_count = 0
    try:
        row_count = int(sys.argv[1])
        print(row_count)
    except:
        print("参数需要是一个正整数") 

    product = ProductData()
    print(product.p.__dict__)
    for i in range(row_count):
        product = ProductData()
        product.p.save()
        print(f'处理记录数量： {i+1}')

    print(f'Current Product count AFTER: {Product.objects.count()}')