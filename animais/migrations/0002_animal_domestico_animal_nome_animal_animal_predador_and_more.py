# Generated by Django 4.1 on 2022-08-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='domestico',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='nome_animal',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='predador',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='venenoso',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
