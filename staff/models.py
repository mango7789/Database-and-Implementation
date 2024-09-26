from django.db import models
from manager.models import shop

class salesman(models.Model):
    id = models.AutoField(primary_key=True)
    salesman_password = models.CharField(max_length=20)
    salesman_name = models.CharField(max_length=10)
    shop_id = models.ForeignKey(to=shop, to_field="id", on_delete=models.PROTECT)
    # avatar = models.ImageField(upload_to="static/avatar/", default="static/avatar/init.png")