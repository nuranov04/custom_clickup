# Generated by Django 4.0.5 on 2022-06-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('redline', models.DateField()),
                ('deadline', models.DateField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('pause', 'pause')], max_length=255)),
            ],
        ),
    ]
