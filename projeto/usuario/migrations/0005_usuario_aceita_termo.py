# Generated by Django 3.0 on 2024-07-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_alter_usuario_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='aceita_termo',
            field=models.BooleanField(default=False, help_text='Se marcado, você aceita o termo de consentimento de uso do sistema', verbose_name='Marque se aceita o termo de consentimento'),
        ),
    ]
