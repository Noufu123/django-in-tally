# Generated by Django 3.2.9 on 2022-09-06 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_purchase_ledgervouchermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direct_GroupSummaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dopeningbalace', models.IntegerField(default=0)),
                ('dperticulars', models.CharField(max_length=250)),
                ('ddebit', models.IntegerField()),
                ('dcredit', models.IntegerField()),
                ('dcompanyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.createcompanymodel')),
            ],
        ),
        migrations.CreateModel(
            name='Direct_ledger_m_summarymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dperticulars', models.CharField(max_length=250)),
                ('ddebit', models.IntegerField()),
                ('dcredit', models.IntegerField()),
                ('dclosingbalance', models.IntegerField()),
                ('dBranchsummary_frgn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.direct_groupsummarymodel')),
            ],
        ),
        migrations.CreateModel(
            name='Direct_ledgervouchermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddate', models.DateField(auto_now_add=True)),
                ('dperticular', models.CharField(max_length=250)),
                ('dvchtype', models.CharField(max_length=250)),
                ('dvchno', models.IntegerField()),
                ('ddebit', models.IntegerField()),
                ('dcredit', models.IntegerField()),
                ('dledgersummary_frgn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.direct_ledger_m_summarymodel')),
            ],
        ),
    ]