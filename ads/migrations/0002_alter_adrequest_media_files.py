# Generated by Django 4.0.3 on 2022-03-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adrequest',
            name='media_files',
            field=models.URLField(blank=True, null=True),
        ),
    ]