# Generated by Django 5.0.2 on 2024-02-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mass', models.FloatField(blank=True, null=True)),
                ('feh', models.FloatField(blank=True, null=True)),
                ('fov', models.FloatField(blank=True, null=True)),
                ('model', models.FloatField(blank=True, null=True)),
                ('logt', models.FloatField(blank=True, null=True)),
                ('logl', models.FloatField(blank=True, null=True)),
                ('pf', models.FloatField(blank=True, null=True)),
                ('ef', models.FloatField(blank=True, null=True)),
                ('p1', models.FloatField(blank=True, null=True)),
                ('e1', models.FloatField(blank=True, null=True)),
                ('p2', models.FloatField(blank=True, null=True)),
                ('e2', models.FloatField(blank=True, null=True)),
                ('p3', models.FloatField(blank=True, null=True)),
                ('e3', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dane',
                'managed': False,
            },
        ),
    ]