# Generated by Django 3.0 on 2019-12-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=100)),
            ],
        ),
    ]