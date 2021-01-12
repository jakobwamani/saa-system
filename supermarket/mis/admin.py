from django.contrib import admin
# from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
# from webcam import widgets
# from webcam.fields import CameraField

# Register your models here.
from mis.models import stock

admin.site.register(stock)


# FORMFIELD_FOR_DBFIELD_DEFAULTS[CameraField] = {'widget': widgets.CameraWidget}

