# Generated by Django 5.0.7 on 2024-07-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_options_menu_named_url_menu_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(help_text='Use it in templatetag for displaying menu', max_length=255, null=True, verbose_name='slug'),
        ),
    ]
