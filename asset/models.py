#-*-coding:utf-8-*-

from __future__ import unicode_literals
from django.db import models
from asset.user_models import UserProfile


class Asset(models.Model):
    asset_type_choices = (
        ('server', u'服务器'),
        ('switch', u'交换机'),
        ('router', u'路由器'),
        ('firewall', u'防火墙'),
        ('software', u'软件'),
        ('wireless', u'无线设备'),
        ('others', u'其他'),
    )

    asset_type = models.CharField(choices=asset_type_choices, max_length=64, default='server')
    name = models.CharField(max_length=64, unique=True)
    sn = models.CharField(u'资产ID', max_length=128, unique=True)
    manufactory = models.CharField(max_length=64, verbose_name=u'制造商', null=True,)
    manager_ip = models.GenericIPAddressField(verbose_name=u'管理ip', null=True, blank=True)
    contract = models.ForeignKey('Contract', verbose_name=u'合同号', null=True, blank=True)
    buying_date = models.DateField(u'购买时间', null=True, blank=True)
    expire_date = models.DateField(u'过保时间', null=True, blank=True)
    price = models.FloatField(u'价格', null=True, blank=True)
    business_unit = models.ForeignKey('BusinessUnit', verbose_name=u'业务线', null=True, blanck=True)
    tags = models.CharField(u'标签', null=True, blank=True)
    admin = models.ForeignKey('UserProfile', verbose_name='资产管理员', null=True, blank=True)
    idc = models.ForeignKey('IDC', verbose_name=u'IDC机房', null=True, blank=True)
    memo = models.TextField(u'备注', null=True, blank=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        verbose_name = u'总资产表'
        verbose_name_plural = u'总资产表'

    def __unicode__(self):
        return 'id:%s name:%s' % (self.id, self.admin)

    