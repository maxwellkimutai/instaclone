# Generated by Django 2.0 on 2018-11-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxigram', '0007_auto_20181109_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.IntegerField()),
                ('liker', models.CharField(max_length=40)),
            ],
        ),
    ]
