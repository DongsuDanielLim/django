# Generated by Django 2.0.13 on 2020-03-15 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postings_published_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postings',
            new_name='Posting',
        ),
    ]
