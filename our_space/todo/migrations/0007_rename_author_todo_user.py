# Generated by Django 4.1.3 on 2022-11-25 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_rename_user_todo_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='author',
            new_name='user',
        ),
    ]
