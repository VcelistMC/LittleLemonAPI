# Generated by Django 4.1.4 on 2022-12-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='littlelemonuser',
            name='qwe',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
