# Generated by Django 3.2.5 on 2021-07-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'галерея',
                'verbose_name_plural': 'галерея',
            },
        ),
    ]
