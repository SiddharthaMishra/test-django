# Generated by Django 3.0.6 on 2020-05-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200507_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='model',
            name='picture',
            field=models.ImageField(default='/media/variant/default.png', upload_to='variant'),
        ),
    ]