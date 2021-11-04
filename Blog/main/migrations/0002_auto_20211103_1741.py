# Generated by Django 3.2.4 on 2021-11-03 17:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=ckeditor.fields.RichTextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.TextField(default=0, verbose_name='Maqola nomi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, default=0, max_length=200, verbose_name='Katigoriya nomi'),
            preserve_default=False,
        ),
    ]
