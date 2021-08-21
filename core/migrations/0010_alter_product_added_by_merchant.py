# Generated by Django 3.2.6 on 2021-08-21 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_remove_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_by_merchant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]