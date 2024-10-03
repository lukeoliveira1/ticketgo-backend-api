# Generated by Django 5.0.4 on 2024-05-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0002_rename_id_user_purchase_user_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('PIX', 'Pix'), ('CREDIT_CARD', 'Cartão de crédito'), ('BOLETO', 'Cartão de crédito'), ('UNDEFINED', 'Cartão de crédito')], max_length=50, verbose_name='Tipo do pagamento'),
        ),
    ]
