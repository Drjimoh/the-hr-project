# Generated by Django 2.2 on 2019-05-06 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvranker', '0002_auto_20190501_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoredCv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
