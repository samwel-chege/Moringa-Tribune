# Generated by Django 3.2.6 on 2021-09-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='no photo', upload_to='articles/'),
        ),
    ]