# Generated by Django 4.1.5 on 2023-01-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_delete_test_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer_detail',
            name='dateofreg',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='lecturer_detail',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
