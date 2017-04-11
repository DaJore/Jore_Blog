# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)  # 博客标题
    tag = models.CharField(max_length=50, blank=True)  # 标签，关键词
    date = models.DateField(auto_now_add=True)  # 日期
    # summary = models.CharField(max_length=200, blank=True)  # 摘要
    # content = models.TextField(blank=True, null=True)  # 正文
    content = UEditorField('content', height=300, width=1000, default=u'',
                           blank=True, toolbars='full')

    # def __unicode__(self):
    #     return self.title

    class Meta:
        ordering = ['-date']
