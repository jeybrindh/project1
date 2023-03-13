# Generated by Django 4.1.5 on 2023-03-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='ccontact',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='cemail',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='cname',
        ),
        migrations.AddField(
            model_name='employee',
            name='uploads',
            field=models.FileField(default=2, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='employee',
            table=None,
        ),
    ]