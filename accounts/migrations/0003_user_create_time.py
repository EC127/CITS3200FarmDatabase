# Generated by Django 4.1.1 on 2022-10-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_id_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Registration time'),
        ),
    ]
