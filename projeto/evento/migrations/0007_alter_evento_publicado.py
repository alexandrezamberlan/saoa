# Generated by Django 4.2.16 on 2024-10-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0006_evento_data_divulgacao_trabalhos_aprovados_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='publicado',
            field=models.BooleanField(default=False, help_text='Se marcada a caixa, os resultados das avaliações serão exibidos aos autores de trabalhos', verbose_name='Resultados publicados'),
        ),
    ]