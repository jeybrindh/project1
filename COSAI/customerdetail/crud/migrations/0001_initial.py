# Generated by Django 4.1.4 on 2022-12-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=20)),
                ('cname', models.CharField(max_length=100)),
                ('cemail', models.EmailField(max_length=254)),
                ('ccontact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]