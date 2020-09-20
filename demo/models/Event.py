import uuid

from django.db import models
from django.utils.encoding import smart_str


class Event(models.Model):
    id = models.CharField(
        '事件ID，通道内唯一',
        default=uuid.uuid1,
        editable=False,
        max_length=36,
        primary_key=True,
    )

    name = models.CharField(
        '事件名称',
        max_length=32,
        editable=False,
    )

    type = models.CharField(
        '事件类型',
        max_length=8,
        choices=(
            ('Tx', 'Tx'),
            ('Config', 'Config'),
            ('Contract', 'Contract'),
            ('Block', 'Block'),
        ),
        editable=False,
    )

    content = models.CharField(
        '当 EventType 为 “Contract” 时，为经过Base64编码的智能合约事件内容',
        max_length=256,
        editable=False,
    )

    class Meta:
        verbose_name = '事件'
        verbose_name_plural = '所有事件'

    def __str__(self):
        return smart_str('%s-%s' % (self.type, self.name))
