# Generated by Django 4.1.2 on 2022-10-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeloconsigoStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('identification', models.CharField(default='DEFAULT VALUE', max_length=20)),
                ('address', models.CharField(default='DEFAULT VALUE', max_length=30)),
                ('phone_Number', models.CharField(default='DEFAULT VALUE', max_length=30)),
                ('email', models.CharField(default='DEFAULT VALUE', max_length=50)),
            ],
            options={
                'db_table': 'TeloconsigoStore',
            },
        ),
    ]
