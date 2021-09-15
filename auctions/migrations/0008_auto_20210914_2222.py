# Generated by Django 3.2.5 on 2021-09-14 14:22

import ckeditor.fields
from decimal import Decimal
from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_lot_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='bid',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=10, validators=[djmoney.models.validators.MinMoneyValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='lot',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]