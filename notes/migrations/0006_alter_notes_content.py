# Generated by Django 3.2.20 on 2023-10-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_notes_last_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]