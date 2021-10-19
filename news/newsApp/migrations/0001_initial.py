# Generated by Django 3.2.8 on 2021-10-09 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('rasm', models.ImageField(blank=True, upload_to='image/')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('ctg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsApp.categorymodel')),
            ],
        ),
    ]
