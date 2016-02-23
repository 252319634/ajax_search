# -*- coding:utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Cnword
from pinyin import PinYin
import json





def index(request):
    #汉字转拼音代码,使用sqllite3数据库太慢,需要几个小时 ,使用mysql只需要不到10分钟.
    #哖嗯媬糬艹韟 这几个字没有拼音检索时会有误差
    # test = PinYin()
    # test.load_word()
    # for i in word:
    #     try:
    #         if i.py:
    #             continue
    #         i.py = test.hanzi2pinyin(string=i.words)
    #         print i,i.py
    #         i.save()
    #     except:
    #         continue
    word = Cnword.objects.all()
    return render_to_response('index.html', locals())


def search(request):
    kw = request.GET.get('kw')
    # print kw
    try:
        str(kw)  # 如果能转成str 就搜索拼音
        word = Cnword.objects.filter(py__startswith=kw).values('words')[0:10]# 查询拼音
    except:
        # 转不成str 就搜索汉字
        word = Cnword.objects.filter(words__startswith=kw).values('words')[0:10]  # 返回django.db.models.query.ValuesQuerySet对象
    # word = Cnword.objects.filter(words__startswith=kw)[0:10]  # 返回django.db.models.query.QuerySet对象
    if word:
        word = list(word)  # ValuesQuerySet对象需要先转换成list
        data = json.dumps(word)  # 把list转成json
        # data = serializers.serialize("json", word) #django.db.models.query.QuerySet对象可以序列化
        return HttpResponse(data)  # 返回json
    return HttpResponse('false')


def match(request):
    kw = request.GET.get('kw')
    try:
        str(kw)
        word = Cnword.objects.filter(py=kw)  # 查询拼音
    except:
        word = Cnword.objects.filter(words=kw)  # 查询汉字
    if word:
        json = serializers.serialize("json", word)
        # print json
        return HttpResponse(json)
    return HttpResponse('false')