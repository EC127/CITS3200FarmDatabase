# Generated by Django 4.1.1 on 2022-09-30 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_pastfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastfile',
            name='fileref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='past_versions', to='files.file'),
        ),
    ]
