# Generated by Django 2.0 on 2018-11-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxigram', '0005_auto_20181109_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
