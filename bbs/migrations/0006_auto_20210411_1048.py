# Generated by Django 2.2.2 on 2021-04-11 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0005_auto_20210410_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='文章摘要'),
        ),
    ]
