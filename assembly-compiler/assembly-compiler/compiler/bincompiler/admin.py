from django.contrib import admin
from .models import CodeSource, Device
# Register your models here.


admin.site.register(Device)
admin.site.register(CodeSource)