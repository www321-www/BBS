from django.contrib import admin

# Register your models here.
from bbs import models

admin.site.register(models.UserInfo)
admin.site.register(models.Blog)
admin.site.register(models.Category)
admin.site.register(models.Article)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
admin.site.register(models.UpAndDown)
