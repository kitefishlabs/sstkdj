# Generated by Django 2.2.6 on 2019-11-04 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundscapes', '0002_auto_20191031_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='regioncircle',
            name='assigned_slot',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='regioncircle',
            name='finish_rule',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='regioncircle',
            name='loops',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='regioncircle',
            name='pause_offset',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='regioncircle',
            name='state',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
