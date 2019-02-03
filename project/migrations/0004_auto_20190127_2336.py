# Generated by Django 2.1.5 on 2019-01-27 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20190108_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road', models.CharField(max_length=120)),
                ('zone_code', models.CharField(blank=True, max_length=5)),
                ('zone', models.CharField(blank=True, max_length=30)),
                ('borough', models.CharField(blank=True, max_length=30)),
                ('suspension_href', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='road',
            unique_together={('road', 'borough', 'zone')},
        ),
    ]