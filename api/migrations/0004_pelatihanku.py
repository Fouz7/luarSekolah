# Generated by Django 5.1 on 2024-09-03 04:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_datapelatihan'),
    ]

    operations = [
        migrations.CreateModel(
            name='PelatihanKu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('pelatihan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.datapelatihan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
