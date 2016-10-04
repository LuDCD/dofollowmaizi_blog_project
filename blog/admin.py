# -*- coding:utf8 -*-


from django.contrib import admin
from models import *

# Register your models here.

# 自定义注册方法
class ArcticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count',)
    # exclude = ('click_count',)
    list_display = ('desc',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag' )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend',),
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

# 默认的注册方法
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArcticleAdmin) # 把自定义的管理类 ArcticleAdmin 注册进来
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)