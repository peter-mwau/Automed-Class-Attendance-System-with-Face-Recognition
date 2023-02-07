# Generated by Django 4.1.5 on 2023-01-31 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student_report',
        ),
        migrations.RenameField(
            model_name='lecturer_report',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='lecturer_report',
            name='dateofattendance',
        ),
        migrations.RemoveField(
            model_name='lecturer_report',
            name='image',
        ),
        migrations.RemoveField(
            model_name='lecturer_report',
            name='lecturer_id',
        ),
        migrations.RemoveField(
            model_name='lecturer_report',
            name='lname',
        ),
        migrations.AddField(
            model_name='lecturer_report',
            name='category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturer_report',
            name='date',
            field=models.DateField(default='2016-09-23'),
        ),
        migrations.AddField(
            model_name='lecturer_report',
            name='department',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturer_report',
            name='faculty',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecturer_report',
            name='unit',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
