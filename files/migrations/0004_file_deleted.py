# Generated by Django 4.1.1 on 2022-09-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_remove_file_paddocks_remove_file_tags_file_paddocks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='deleted',
            field=models.IntegerField(default=0),
        ),
    ]
