# Generated by Django 4.0.5 on 2022-06-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf_name', models.CharField(max_length=60)),
                ('uf_initials', models.CharField(max_length=2)),
            ],
        ),
    ]
