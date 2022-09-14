# Generated by Django 3.2.9 on 2022-09-08 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_auto_20220907_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bledgersummarypagemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bperticulars', models.CharField(max_length=250)),
                ('bdebit', models.IntegerField()),
                ('bcredit', models.IntegerField()),
                ('bclosingbalance', models.IntegerField()),
                ('Branchsummary_frgn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.branchgroupsummarymodel')),
            ],
        ),
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
            name='Purchase_ledger_m_summarymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pperticulars', models.CharField(max_length=250)),
                ('pdebit', models.IntegerField()),
                ('pcredit', models.IntegerField()),
                ('pclosingbalance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='salesGroupSummaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sopeningbalace', models.IntegerField(default=0)),
                ('sperticulars', models.CharField(max_length=250)),
                ('sdebit', models.IntegerField()),
                ('scredit', models.IntegerField()),
                ('scompanyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.createcompanymodel')),
            ],
        ),
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
        migrations.CreateModel(
            name='PurchaseGroupSummaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popeningbalace', models.IntegerField(default=0)),
                ('pperticulars', models.CharField(max_length=250)),
                ('pdebit', models.IntegerField()),
                ('pcredit', models.IntegerField()),
                ('pcompanyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.createcompanymodel')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_ledgervouchermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdate', models.DateField(auto_now_add=True)),
                ('pperticular', models.CharField(max_length=250)),
                ('pvchtype', models.CharField(max_length=250)),
                ('pvchno', models.IntegerField()),
                ('pdebit', models.IntegerField()),
                ('pcredit', models.IntegerField()),
                ('pledgersummary_frgn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.purchase_ledger_m_summarymodel')),
            ],
        ),
        migrations.AddField(
            model_name='purchase_ledger_m_summarymodel',
            name='pBranchsummary_frgn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.purchasegroupsummarymodel'),
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
        migrations.CreateModel(
            name='bledgervouchermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bdate', models.DateField(auto_now_add=True)),
                ('bperticular', models.CharField(max_length=250)),
                ('bvchtype', models.CharField(max_length=250)),
                ('bvchno', models.IntegerField()),
                ('bdebit', models.IntegerField()),
                ('bcredit', models.IntegerField()),
                ('bledgersummary_frgn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.bledgersummarypagemodel')),
            ],
        ),
    ]