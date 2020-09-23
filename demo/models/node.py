import uuid

from django.db import models
from django.utils.encoding import smart_str


class Node(models.Model):
    id = models.CharField(
        '节点ID',
        primary_key=True,
        default=uuid.uuid1,
        max_length=36,
    )

    parsed_url = models.URLField(
        '节点的URL',
        unique=True,
    )

    class Meta:
        verbose_name = '节点'
        verbose_name_plural = '所有节点'

    def __str__(self):
        return self.parsed_url



