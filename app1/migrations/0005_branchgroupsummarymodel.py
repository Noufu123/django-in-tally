# Generated by Django 3.2.9 on 2022-09-03 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20220902_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchGroupSummaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bperticulars', models.CharField(max_length=250)),
                ('bdebit', models.IntegerField()),
                ('bcredit', models.IntegerField()),
                ('companyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.createcompanymodel')),
            ],
        ),
    ]
