# Generated by Django 4.2.7 on 2024-04-15 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_order_options_alter_order_status_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Родительская категория'),
        ),
    ]
