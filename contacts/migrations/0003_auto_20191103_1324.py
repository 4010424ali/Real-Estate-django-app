# Generated by Django 2.2.6 on 2019-11-03 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20191103_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='lsiting',
            new_name='listing',
        ),
    ]