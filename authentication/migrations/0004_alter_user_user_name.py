# Generated by Django 3.2.20 on 2023-09-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_name_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, default='Unknown', max_length=255),
            preserve_default=False,
        ),
    ]
