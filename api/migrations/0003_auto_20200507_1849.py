# Generated by Django 3.0.6 on 2020-05-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200507_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='picture',
            field=models.ImageField(default='/media/variat/default.png', upload_to='model'),
        ),
    ]
