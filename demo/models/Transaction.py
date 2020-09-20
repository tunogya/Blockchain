import uuid

from django.db import models


class Transaction(models.Model):
    id = models.CharField(
        '交易ID',
        primary_key=True,
        default=uuid.uuid1,
        max_length=36,
        editable=False,
    )

    state = models.CharField(
        '交易状态，”VALID” 表示合法交易，其它值表示非法交易',
        max_length=12,
        blank=True,
        null=True,
        editable=False,
    )

    events = models.JSONField(
        '交易所产生的区块链事件列表',
        editable=False,
    )

    data = models.JSONField(
        '交易的详细内容，数据结构为交易中的 common.Payload',
        editable=False,
    )

    class Meta:
        verbose_name = '交易'
        verbose_name_plural = '所有交易'

