# Generated by Django 4.1.5 on 2023-01-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_student_detail_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='dateofreg',
            field=models.DateField(default='e.g 2021-09-12'),
        ),
    ]
