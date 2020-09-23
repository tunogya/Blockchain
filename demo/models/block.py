from django.db import models
from django.utils.encoding import smart_str


class Block(models.Model):
    index = models.IntegerField(
        '区块块高',
        primary_key=True,
        auto_created=True,
    )

    hash = models.CharField(
        'hex 编码后的当前区块 hash 值',
        max_length=64,
    )

    previous_hash = models.CharField(
        'hex 编码后的上一区块 hash 值',
        max_length=64,
    )

    create_time = models.IntegerField(
        '当前区块创建时间，Unix秒级时间戳',
    )

    transactions = models.JSONField(
        '当前区块中，包含的所有交易的交易ID列表',
    )

    proof = models.IntegerField(
        '工作量证明',
    )

    class Meta:
        verbose_name = "区块"
        verbose_name_plural = "所有区块"

    def __str__(self):
        return smart_str('%d-%s' % (self.id, self.hash))
