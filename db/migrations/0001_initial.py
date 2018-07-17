# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-16 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default='', max_length=255, unique=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('email', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'client',
                'verbose_name': 'client',
            },
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cluster',
                'verbose_name': 'cluster',
            },
        ),
        migrations.CreateModel(
            name='HistoryPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'history_place',
                'verbose_name': 'history_place',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('ip', models.CharField(default='', max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'host',
                'verbose_name': 'host',
            },
        ),
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'pod',
                'verbose_name': 'pod',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('display_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'site',
                'verbose_name': 'site',
            },
        ),
        migrations.CreateModel(
            name='VC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('ip', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('port', models.IntegerField(blank=True, default=443, null=True)),
                ('username', models.CharField(blank=True, default='ops.user01', max_length=255, null=True)),
                ('password', models.CharField(blank=True, default='cds-P@$$w0rd@2017', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'vc',
                'verbose_name': 'vc',
            },
        ),
        migrations.CreateModel(
            name='VM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='db.Client')),
            ],
            options={
                'db_table': 'vm',
                'verbose_name': 'vm',
            },
        ),
        migrations.AddField(
            model_name='pod',
            name='site',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Site'),
        ),
        migrations.AddField(
            model_name='pod',
            name='vc',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='db.VC'),
        ),
        migrations.AddField(
            model_name='historyplace',
            name='place1',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_current', to='db.Host'),
        ),
        migrations.AddField(
            model_name='historyplace',
            name='place2',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_last_1', to='db.Host'),
        ),
        migrations.AddField(
            model_name='historyplace',
            name='place3',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_last_2', to='db.Host'),
        ),
        migrations.AddField(
            model_name='historyplace',
            name='place4',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_last_3', to='db.Host'),
        ),
        migrations.AddField(
            model_name='historyplace',
            name='place5',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_last_4', to='db.Host'),
        ),
        migrations.AddField(
            model_name='historyplace',
            name='vm',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='db.VM'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='pod',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Pod'),
        ),
    ]
