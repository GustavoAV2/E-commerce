# Generated by Django 3.2 on 2021-05-05 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=300, null=True, verbose_name='description'),
        ),
    ]
