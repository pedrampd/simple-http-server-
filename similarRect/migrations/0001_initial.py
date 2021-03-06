# Generated by Django 3.2.5 on 2021-07-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rectangle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('time_created', models.DateTimeField()),
                ('included', models.BooleanField()),
                ('main', models.BooleanField()),
            ],
        ),
    ]
