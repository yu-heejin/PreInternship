# Generated by Django 4.0.2 on 2022-02-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdb', '0006_alter_img_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='imgUrl',
            field=models.ImageField(upload_to='pic'),
        ),
    ]