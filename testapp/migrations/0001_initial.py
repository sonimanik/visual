# Generated by Django 2.1.7 on 2019-03-23 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=64)),
                ('eno', models.IntegerField()),
                ('esal', models.FloatField()),
            ],
        ),
    ]