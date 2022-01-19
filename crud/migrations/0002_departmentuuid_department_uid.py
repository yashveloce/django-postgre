# Generated by Django 4.0 on 2021-12-31 06:09

import crud.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentUUID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuidNumber', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='uId',
            field=models.CharField(default=crud.models.getDepartmentUUID, max_length=10, unique=True),
        ),
    ]
