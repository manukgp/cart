# Generated by Django 3.2.12 on 2023-08-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20230821_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
