# Generated by Django 3.2.4 on 2022-02-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newProduct', '0009_auto_20220211_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Weight', 'Weight'), ('Height', 'Height'), ('Length', 'Length'), ('Width', 'Width'), ('Size-Color', 'Size-Color'), ('Wght-Color', 'Weight-Color')], default='None', max_length=10),
        ),
    ]
