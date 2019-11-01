# Generated by Django 2.2.6 on 2019-10-31 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Soundfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='default', max_length=100)),
                ('filepath', models.CharField(default='default.wav', max_length=200)),
                ('length', models.IntegerField(default=48000)),
                ('sample_rate', models.IntegerField(default=48000)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegionMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegionCircle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(blank=True, default='', max_length=100)),
                ('center_latitude', models.FloatField(default=0.0, verbose_name='latitude')),
                ('center_longitude', models.FloatField(default=0.0, verbose_name='longitude')),
                ('radius', models.FloatField(default=0.01)),
                ('active', models.BooleanField(default=True)),
                ('attack', models.IntegerField(default=1000)),
                ('release', models.IntegerField(default=1000)),
                ('lives', models.IntegerField(default=99)),
                ('region_map', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='soundscapes.RegionMap')),
                ('soundfile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='soundscapes.Soundfile')),
            ],
        ),
    ]
