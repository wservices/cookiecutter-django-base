# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('postal_code', models.CharField(max_length=100, verbose_name='Postal code')),
                ('place', models.CharField(max_length=100, verbose_name='Place/City')),
                ('country_code', models.CharField(default='CH', max_length=2, verbose_name='Country code')),
                ('country_name', models.CharField(default='Switzerland', max_length=100, verbose_name='Country')),
                ('iban', models.CharField(blank=True, max_length=42, verbose_name='IBAN')),
                ('number', models.CharField(blank=True, max_length=42, verbose_name='Number')),
                ('bic', models.CharField(blank=True, max_length=11, verbose_name='BIC')),
                ('currency_code', models.CharField(default='CHF', max_length=3, verbose_name='Currency ISO code')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sites.Site')),
                ('company_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Company name')),
                ('company_department', models.CharField(blank=True, max_length=50, verbose_name='Company department')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('postal_code', models.CharField(max_length=100, verbose_name='Postal code')),
                ('place', models.CharField(max_length=100, verbose_name='Place/City')),
                ('country_code', models.CharField(default='CH', max_length=2, verbose_name='Country code')),
                ('country_name', models.CharField(default='Switzerland', max_length=100, verbose_name='Country')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone')),
                ('fax', models.CharField(blank=True, max_length=32, null=True, verbose_name='Fax')),
                ('vat_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='VAT number')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='ownership', verbose_name='Logo')),
                ('logo_invoice', models.ImageField(blank=True, null=True, upload_to='ownership', verbose_name='Logo invoice')),
                ('stripe_public_key', models.CharField(blank=True, max_length=32, null=True, verbose_name='Stripe public key')),
            ],
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankaccounts', to='imprint.Ownership'),
        ),
    ]