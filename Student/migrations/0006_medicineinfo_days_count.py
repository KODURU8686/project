# Generated by Django 3.0 on 2021-05-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_auto_20210513_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicineinfo',
            name='days_count',
            field=models.DateField(null=True),
        ),
    ]
