# Generated by Django 4.1.2 on 2022-10-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
