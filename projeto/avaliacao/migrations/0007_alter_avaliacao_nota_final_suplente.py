# Generated by Django 4.2.16 on 2024-10-21 14:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0006_alter_avaliacao_media_final_avaliacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota_final_suplente',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5)], verbose_name='Final Avaliador 2'),
        ),
    ]