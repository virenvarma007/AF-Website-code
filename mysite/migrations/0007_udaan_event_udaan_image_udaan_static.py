# Generated by Django 2.2.13 on 2020-10-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_blog_blog_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Udaan_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Udaan_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images/udaan/carousel')),
                ('alt_text', models.CharField(max_length=50)),
                ('display_on_caurosel', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Udaan_static',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_description', models.TextField()),
                ('bg_pic', models.ImageField(upload_to='images/udaan/background')),
                ('date', models.DateTimeField(default='2020-01-01')),
            ],
        ),
    ]