# Generated by Django 4.0.6 on 2022-07-18 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(error_messages={'blank': "The company_id field can't be blank.", 'invalid': 'The company_id field is invalid.', 'null': "The company_id field can't be null."}, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.company'),
        ),
    ]
