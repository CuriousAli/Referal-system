# Generated by Django 3.2.3 on 2021-05-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='my_ref',
            field=models.CharField(default=None, max_length=6, unique=True),
        ),
    ]
