# Generated by Django 4.1.5 on 2023-02-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_alter_lecturer_report_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer_report',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]