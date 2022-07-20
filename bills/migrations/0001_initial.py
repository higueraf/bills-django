# Generated by Django 4.0.6 on 2022-07-19 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0004_alter_client_municipality_alter_client_parish_and_more'),
        ('common', '0002_alter_state_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The subtotal field is invalid.'}, max_digits=10, null=True, verbose_name='Subtotal')),
                ('tax', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The tax field is invalid.'}, max_digits=10, null=True, verbose_name='Tax')),
                ('total', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The total field is invalid.'}, max_digits=10, null=True, verbose_name='Total')),
                ('client', models.ForeignKey(error_messages={'blank': "The client_id field can't be blank.", 'invalid': 'The client_id field is invalid.', 'null': "The client_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='companies.client')),
                ('company', models.ForeignKey(error_messages={'blank': "The company_id field can't be blank.", 'invalid': 'The company_id field is invalid.', 'null': "The company_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='companies.company')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(error_messages={'blank': "The name field can't be blank.", 'invalid': 'The name field is invalid.', 'max_length': 'The name field must be at most 255 characters.', 'null': "The name field can't be null.", 'unique': 'TypePayment with this name already exists.'}, max_length=255, unique=True, verbose_name='Name')),
                ('description', models.TextField(error_messages={'blank': "The description field can't be blank.", 'invalid': 'The description field is invalid.', 'max_length': 'The description field must be at most 255 characters.', 'null': "The description field can't be null."}, max_length=500, verbose_name='Description')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(error_messages={'blank': "The name field can't be blank.", 'invalid': 'The name field is invalid.', 'max_length': 'The name field must be at most 255 characters.', 'null': "The name field can't be null."}, max_length=255, verbose_name='Name')),
                ('description', models.TextField(error_messages={'blank': "The description field can't be blank.", 'invalid': 'The description field is invalid.', 'max_length': 'The description field must be at most 255 characters.', 'null': "The description field can't be null."}, max_length=500, verbose_name='Description')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The percent field is invalid.'}, max_digits=8, null=True, verbose_name='Percent')),
                ('company', models.ForeignKey(error_messages={'blank': "The company_id field can't be blank.", 'invalid': 'The company_id field is invalid.', 'null': "The company_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='companies.company')),
                ('tax', models.ForeignKey(error_messages={'blank': "The tax_id field can't be blank.", 'invalid': 'The tax_id field is invalid.', 'null': "The tax_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='common.tax')),
                ('user', models.ForeignKey(error_messages={'blank': "The user_id field can't be blank.", 'invalid': 'The user_id field is invalid.', 'null': "The user_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('tax_percent', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The tax_percent field is invalid.'}, max_digits=10, null=True, verbose_name='Tax Percent')),
                ('qty', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The qty field is invalid.'}, max_digits=10, null=True, verbose_name='Qty')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The unit_price field is invalid.'}, max_digits=10, null=True, verbose_name='Price Unit')),
                ('unit_price_with_tax', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The unit_price_with_tax field is invalid.'}, max_digits=10, null=True, verbose_name='Price Unit With Tax')),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The subtotal field is invalid.'}, max_digits=10, null=True, verbose_name='Subtotal')),
                ('subtotal_with_tax', models.DecimalField(blank=True, decimal_places=2, error_messages={'invalid': 'The subtotal_with_tax field is invalid.'}, max_digits=10, null=True, verbose_name='Subtotal with Tax')),
                ('bill', models.ForeignKey(error_messages={'blank': "The bill_id field can't be blank.", 'invalid': 'The bill_id field is invalid.', 'null': "The bill_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, related_name='bill_details', to='bills.bill')),
                ('tax', models.ForeignKey(error_messages={'blank': "The tax_id field can't be blank.", 'invalid': 'The tax_id field is invalid.', 'null': "The tax_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='common.tax')),
                ('user', models.ForeignKey(error_messages={'blank': "The user_id field can't be blank.", 'invalid': 'The user_id field is invalid.', 'null': "The user_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='type_payment',
            field=models.ForeignKey(error_messages={'blank': "The type_payment_id field can't be blank.", 'invalid': 'The type_payment_id field is invalid.', 'null': "The type_payment_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='bills.typepayment'),
        ),
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(error_messages={'blank': "The user_id field can't be blank.", 'invalid': 'The user_id field is invalid.', 'null': "The user_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
