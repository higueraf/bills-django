# Generated by Django 4.0.6 on 2022-07-18 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(error_messages={'blank': "The Name field can't be blank.", 'invalid': 'The Name field is invalid.', 'max_length': 'The Name field must be at most 255 characters.', 'null': "The Name field can't be null."}, max_length=255, verbose_name='Name')),
                ('description', models.TextField(error_messages={'blank': "The description field can't be blank.", 'invalid': 'The description field is invalid.', 'max_length': 'The description field must be at most 255 characters.', 'null': "The description field can't be null."}, max_length=500, verbose_name='Description')),
                ('identification', models.CharField(error_messages={'blank': "The identification field can't be blank.", 'invalid': 'The identification field is invalid.', 'max_length': 'The identification field must be at most 255 characters.', 'null': "The identification field can't be null."}, max_length=100, verbose_name='Identification')),
                ('address', models.TextField(error_messages={'blank': "The address field can't be blank.", 'invalid': 'The address field is invalid.', 'max_length': 'The address field must be at most 255 characters.', 'null': "The address field can't be null."}, max_length=500, verbose_name='Address')),
                ('country', models.ForeignKey(error_messages={'blank': "The user_id field can't be blank.", 'invalid': 'The user_id field is invalid.', 'null': "The user_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='common.country')),
                ('municipality', models.ForeignKey(error_messages={'blank': "The municipality_id field can't be blank.", 'invalid': 'The municipality_id field is invalid.', 'null': "The municipality_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='common.municipality')),
                ('parish', models.ForeignKey(error_messages={'blank': "The parish_id field can't be blank.", 'invalid': 'The parish_id field is invalid.', 'null': "The parish_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='common.parish')),
                ('state', models.ForeignKey(error_messages={'blank': "The state_id field can't be blank.", 'invalid': 'The state_id field is invalid.', 'null': "The state_id field can't be null."}, on_delete=django.db.models.deletion.PROTECT, to='common.state')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
