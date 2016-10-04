#!/usr/bin/python
# -*- coding:utf8 -*-


import logging

from django.conf import settings

from django.shortcuts import render

logger = logging.getLogger('blog.views')
# 日志器
# 导入logging, 定义日志器, 日志器的名字对应你在setting中定义的名字

# Create your views here.

def global_setting(request):
    return {
        'SITE_NAME' : settings.SITE_NAME,
        'SITE_DESC' : settings.SITE_DESC,
        'WEIBO_SINA' : settings.WEIBO_SINA,
        'WEIBO_TENCENT' : settings.WEIBO_TENCENT,
        'EMAIL' : settings.EMAIL,
        'RSS' : settings.RSS,
    }

def index(request):
    # 使用日志器
    try:
        # file = open('sss.txt', 'r') # 例子
        pass
    except Exception as e:
        logger.error(e)     # 出现异常调用日志器，写入日志

    return render(request, 'index.html', locals())