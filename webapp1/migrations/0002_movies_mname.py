# Generated by Django 5.0 on 2023-12-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='mname',
            field=models.CharField(default='Movie', max_length=250),
            preserve_default=False,
        ),
    ]
