# Generated by Django 5.0.4 on 2024-04-09 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_journal', '0003_delete_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school_journal.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school_journal.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school_journal.userprofile')),
            ],
        ),
    ]
