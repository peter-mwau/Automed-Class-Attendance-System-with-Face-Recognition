# Generated by Django 4.1.5 on 2023-01-31 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_lecturer_report_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer_report',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]