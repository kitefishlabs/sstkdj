# Generated by Django 2.2.6 on 2019-11-08 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundscapes', '0007_auto_20191106_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundfile',
            name='analyzed',
            field=models.BooleanField(default=False),
        ),
    ]