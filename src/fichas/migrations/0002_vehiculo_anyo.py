# Generated by Django 2.2.5 on 2019-10-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='anyo',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
