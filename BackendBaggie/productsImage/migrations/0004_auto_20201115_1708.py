# Generated by Django 3.1.1 on 2020-11-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsImage', '0003_productimage_imagename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
