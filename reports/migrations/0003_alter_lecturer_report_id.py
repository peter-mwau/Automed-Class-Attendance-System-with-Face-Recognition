# Generated by Django 4.1.5 on 2023-01-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_delete_student_report_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer_report',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]