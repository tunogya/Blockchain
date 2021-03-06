# Generated by Django 3.1.1 on 2020-09-23 13:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('index', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='区块块高')),
                ('hash', models.CharField(max_length=64, verbose_name='hex 编码后的当前区块 hash 值')),
                ('previous_hash', models.CharField(max_length=64, verbose_name='hex 编码后的上一区块 hash 值')),
                ('create_time', models.IntegerField(verbose_name='当前区块创建时间，Unix秒级时间戳')),
                ('transactions', models.JSONField(verbose_name='当前区块中，包含的所有交易的交易ID列表')),
                ('proof', models.IntegerField(verbose_name='工作量证明')),
            ],
            options={
                'verbose_name': '区块',
                'verbose_name_plural': '所有区块',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(default=uuid.uuid1, editable=False, max_length=36, primary_key=True, serialize=False, verbose_name='事件ID，通道内唯一')),
                ('name', models.CharField(max_length=32, verbose_name='事件名称')),
                ('type', models.CharField(choices=[('Tx', 'Tx'), ('Config', 'Config'), ('Contract', 'Contract'), ('Block', 'Block')], max_length=8, verbose_name='事件类型')),
                ('content', models.CharField(max_length=256, verbose_name='当 EventType 为 “Contract” 时，为经过Base64编码的智能合约事件内容')),
            ],
            options={
                'verbose_name': '事件',
                'verbose_name_plural': '所有事件',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.CharField(default=uuid.uuid1, max_length=36, primary_key=True, serialize=False, verbose_name='节点ID')),
                ('parsed_url', models.URLField(unique=True, verbose_name='节点的URL')),
            ],
            options={
                'verbose_name': '节点',
                'verbose_name_plural': '所有节点',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.CharField(default=uuid.uuid1, max_length=36, primary_key=True, serialize=False, verbose_name='交易ID')),
                ('state', models.CharField(blank=True, max_length=12, null=True, verbose_name='交易状态，”VALID” 表示合法交易，其它值表示非法交易')),
                ('events', models.JSONField(verbose_name='交易所产生的区块链事件列表')),
                ('data', models.JSONField(verbose_name='交易的详细内容，数据结构为交易中的 common.Payload')),
            ],
            options={
                'verbose_name': '交易',
                'verbose_name_plural': '所有交易',
            },
        ),
    ]
