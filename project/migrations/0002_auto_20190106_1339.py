# Generated by Django 2.1.5 on 2019-01-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('IT', 'IT'), ('teaching', 'Teaching'), ('banking', 'Banking'), ('marketing', 'Marketing')], default='IT', max_length=20),
        ),
    ]