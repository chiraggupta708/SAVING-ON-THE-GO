# Generated by Django 3.1.2 on 2020-10-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmoney_info',
            name='money',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='addmoney_info',
            name='add_money',
            field=models.CharField(default='', max_length=10),
        ),
    ]
