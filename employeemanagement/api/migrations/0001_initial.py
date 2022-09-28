# Generated by Django 4.1.1 on 2022-09-24 19:10

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
                ('first_name', models.CharField(blank=True, max_length=26)),
                ('middle_name', models.CharField(blank=True, max_length=26)),
                ('date_of_graduation', models.DateField(null=True)),
                ('date_of_employment', models.DateField(null=True)),
                ('position', models.CharField(blank=True, max_length=20)),
                ('salary', models.IntegerField(default=True)),
                ('supervisors', models.CharField(blank=True, max_length=26)),
            ],
        ),
    ]