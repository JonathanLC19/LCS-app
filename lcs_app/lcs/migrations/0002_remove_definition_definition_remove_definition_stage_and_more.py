# Generated by Django 4.1.3 on 2022-11-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='definition',
            name='definition',
        ),
        migrations.RemoveField(
            model_name='definition',
            name='stage',
        ),
        migrations.AlterField(
            model_name='stage',
            name='stage_name',
            field=models.CharField(max_length=75),
        ),
    ]
