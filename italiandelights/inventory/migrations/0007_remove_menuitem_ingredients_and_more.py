# Generated by Django 4.2.1 on 2023-08-22 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_menuitemingredient_delete_recipe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='ingredients',
        ),
        migrations.DeleteModel(
            name='MenuItemIngredient',
        ),
    ]
