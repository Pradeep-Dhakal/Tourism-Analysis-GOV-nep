# Generated by Django 2.0.7 on 2019-08-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(max_length=1000)),
                ('pagelocation', models.TextField(max_length=1000)),
            ],
        ),
    ]