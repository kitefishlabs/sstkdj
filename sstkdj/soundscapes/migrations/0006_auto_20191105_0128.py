# Generated by Django 2.2.6 on 2019-11-05 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soundscapes', '0005_regioncircle_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regioncircle',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_regions', to=settings.AUTH_USER_MODEL),
        ),
    ]
