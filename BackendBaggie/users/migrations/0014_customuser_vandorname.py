# Generated by Django 3.1.1 on 2020-11-02 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_customuser_vandorname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='vandorName',
            field=models.CharField(max_length=350, null=True, unique=True),
        ),
    ]