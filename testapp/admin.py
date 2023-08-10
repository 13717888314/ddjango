from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User


# Register your models here.

@admin.register(User)
class User(admin.ModelAdmin):
    # 设置页面可以展示的字段
    # get_image_tag 是在模型中设置的显示图片函数，一定要添加上 不然后台不会显示
    list_display = ('username', 'head_img', 'get_image_tag')
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    list_display_links = ('username',)