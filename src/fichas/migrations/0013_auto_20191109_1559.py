# Generated by Django 2.2.5 on 2019-11-09 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0012_auto_20191109_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]