# Generated by Django 3.1.1 on 2020-09-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='create_time',
            field=models.IntegerField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='block',
            name='hash',
            field=models.CharField(max_length=64, verbose_name='当前区块 hash 值'),
        ),
        migrations.AlterField(
            model_name='block',
            name='previous_hash',
            field=models.CharField(max_length=64, verbose_name='上一区块 hash 值'),
        ),
        migrations.AlterField(
            model_name='block',
            name='transactions',
            field=models.JSONField(verbose_name='所有交易的交易ID列表'),
        ),
    ]