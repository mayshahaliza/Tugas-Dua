# Generated by Django 4.1 on 2022-09-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('date', models.TextField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
