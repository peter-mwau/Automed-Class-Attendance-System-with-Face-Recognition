# Generated by Django 4.1.5 on 2023-01-29 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_alter_lecturer_detail_dateofreg'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer_detail',
            name='category',
            field=models.CharField(default='Lecturer', max_length=100),
        ),
    ]