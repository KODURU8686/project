# Generated by Django 3.0 on 2021-05-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_medicineinfo_current_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicineinfo',
            name='current_date',
        ),
        migrations.AddField(
            model_name='medicineinfo',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
