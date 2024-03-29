# Generated by Django 4.2.9 on 2024-01-19 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chain_stores', '0008_alter_supplier_parent_alter_supplier_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='contacts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chain_stores.contacts', verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='type',
            field=models.CharField(choices=[('Завод', 'Zavod'), ('ИП', 'Ip'), ('Розничная сеть', 'Rc')], default='Завод', verbose_name='Тип'),
        ),
    ]
