# Generated by Django 3.1.2 on 2020-10-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0003_historicaldata_case_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaldata',
            name='predicted_disease',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
