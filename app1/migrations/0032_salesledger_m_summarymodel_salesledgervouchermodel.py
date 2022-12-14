# Generated by Django 3.2.9 on 2022-09-08 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_auto_20220908_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='salesledger_m_summarymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sperticulars', models.CharField(max_length=250)),
                ('sdebit', models.IntegerField()),
                ('scredit', models.IntegerField()),
                ('sclosingbalance', models.IntegerField()),
                ('sBranchsummary_frgn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.salesgroupsummarymodel')),
            ],
        ),
        migrations.CreateModel(
            name='salesledgervouchermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdate', models.DateField(auto_now_add=True)),
                ('sperticular', models.CharField(max_length=250)),
                ('svchtype', models.CharField(max_length=250)),
                ('svchno', models.IntegerField()),
                ('sdebit', models.IntegerField()),
                ('scredit', models.IntegerField()),
                ('sledgersummary_frgn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.salesledger_m_summarymodel')),
            ],
        ),
    ]
