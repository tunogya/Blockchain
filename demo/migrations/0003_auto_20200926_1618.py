# Generated by Django 3.1.1 on 2020-09-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200926_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='index',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='区块块高'),
        ),
    ]