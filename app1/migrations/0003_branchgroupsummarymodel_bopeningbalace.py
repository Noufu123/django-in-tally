# Generated by Django 3.2.9 on 2022-09-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_bledgersummarypagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchgroupsummarymodel',
            name='bopeningbalace',
            field=models.IntegerField(default=0),
        ),
    ]
