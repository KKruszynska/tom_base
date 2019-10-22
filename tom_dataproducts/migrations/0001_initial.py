# Generated by Django 2.1.4 on 2019-02-14 17:24

import datetime

from django.db import migrations, models
import django.db.models.deletion
import tom_dataproducts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tom_observations', '0001_initial'),
        ('tom_targets', '0004_auto_20190123_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=255, null=True, unique=True)),
                ('data', models.FileField(default=None, null=True, upload_to=tom_dataproducts.models.data_product_path)),
                ('extra_data', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(blank=True, choices=[('photometry', 'Photometry'), ('fits_file', 'Fits File'), ('spectroscopy', 'Spectroscopy')], default='', max_length=50)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
                'get_latest_by': ('modified',),
            },
        ),
        migrations.CreateModel(
            name='DataProductGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ReducedDatum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_type', models.CharField(choices=[('SPECTROSCOPY', 'Spectroscopy'), ('PHOTOMETRY', 'Photometry')], default='', max_length=100)),
                ('source_name', models.CharField(default='', max_length=100)),
                ('source_location', models.CharField(default='', max_length=200)),
                ('timestamp', models.DateTimeField(db_index=True, default=datetime.datetime.now)),
                ('value', models.TextField()),
                ('data_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tom_dataproducts.DataProduct')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tom_targets.Target')),
            ],
        ),
        migrations.AddField(
            model_name='dataproduct',
            name='group',
            field=models.ManyToManyField(to='tom_dataproducts.DataProductGroup'),
        ),
        migrations.AddField(
            model_name='dataproduct',
            name='observation_record',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tom_observations.ObservationRecord'),
        ),
        migrations.AddField(
            model_name='dataproduct',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tom_targets.Target'),
        ),
    ]
