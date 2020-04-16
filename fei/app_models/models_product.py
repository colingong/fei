"""产品相关的模型：产品类目和产品 
   Category: 类目
   Product: 具体产品
"""

from django.db import models
class Supplier(models.Model):
    """供应商
    
    Arguments:
        models {[type]} -- [description]
    """
    supplier_name = models.CharField(max_length=100)
    supplier_code = models.CharField(max_length=50)
    supplier_type = models.CharField(max_length=50)
    def __str__(self):
        return f' {self.supplier_code} {self.supplier_name}'

class Warehouse(models.Model):
    """仓库信息配置
       :warehouse_type_name: 仓库名称
       :warehouse_code: 仓库代码
    """
    warehouse_type_name = models.CharField(max_length=100, unique=True)
    warehouse_code = models.CharField(max_length=50, unique=True)
    warehouse_address = models.CharField(max_length=250)
    
    def __str__(self):
        return f'{self.warehouse_type_code} {self.warehouse_type_name}'

class Category(models.Model):
    """类目的模型
    :用于配置可用的产品类目。
    
    """
    category_type_name = models.CharField(max_length=100)
    category_type_code = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.category_type_code} {self.category_type_name}'

class Product(models.Model):
    """产品列表，包含了所有的产品
    
    Arguments:
        models {[type]} -- [description]
    """
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=500)
    product_price = models.DecimalField(max_digits=18, decimal_places=2)
    product_stock = models.IntegerField(default=0)
    for_sale = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product_name}'