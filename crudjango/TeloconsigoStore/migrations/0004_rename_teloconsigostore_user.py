# Generated by Django 4.1.2 on 2022-10-05 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TeloconsigoStore', '0003_alter_teloconsigostore_address_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeloconsigoStore',
            new_name='User',
        ),
    ]