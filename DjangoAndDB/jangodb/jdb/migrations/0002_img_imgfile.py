# Generated by Django 4.0.2 on 2022-02-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='imgFile',
            field=models.ImageField(null=True, upload_to='items'),
        ),
    ]
