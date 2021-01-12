from django.db import models
from datetime import date
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
# import webcam.admin # needed to show the right widget in the admin
# from webcam.fields import CameraField
# from webcam.fields import DBCameraField, FSCameraField
# from webcam.storage import CameraFileSystemStorage
class stock(models.Model):
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    category = models.CharField(max_length=200)
    selling_price = models.IntegerField(default=0)
    pub_date = models.DateField(default=date.today)
    barcode = models.ImageField(upload_to='images/',blank=True)
    def __str__(self):
        return self.product_name

    def save(self,*args,**kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN('5901234123457', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png',File(buffer),save=False)
        return super().save(*args,**kwargs)    




 