# Generated by Django 4.1.1 on 2022-09-25 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_employee_id_alter_employee_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='date_of_employment',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_of_graduation',
        ),
    ]
