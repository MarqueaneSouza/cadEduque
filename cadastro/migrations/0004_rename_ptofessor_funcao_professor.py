# Generated by Django 5.0 on 2023-12-16 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_rename_cadastro_funcao_ptofessor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcao',
            old_name='ptofessor',
            new_name='professor',
        ),
    ]
