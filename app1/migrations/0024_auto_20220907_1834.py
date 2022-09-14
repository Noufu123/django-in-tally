# Generated by Django 3.2.9 on 2022-09-08 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_createmonthmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bledgervouchermodel',
            name='bledgersummary_frgn',
        ),
        migrations.RemoveField(
            model_name='direct_groupsummarymodel',
            name='dcompanyname',
        ),
        migrations.RemoveField(
            model_name='direct_ledger_m_summarymodel',
            name='dBranchsummary_frgn',
        ),
        migrations.RemoveField(
            model_name='direct_ledgervouchermodel',
            name='dledgersummary_frgn',
        ),
        migrations.RemoveField(
            model_name='purchase_ledger_m_summarymodel',
            name='pBranchsummary_frgn',
        ),
        migrations.RemoveField(
            model_name='purchase_ledgervouchermodel',
            name='pledgersummary_frgn',
        ),
        migrations.RemoveField(
            model_name='purchasegroupsummarymodel',
            name='pcompanyname',
        ),
        migrations.RemoveField(
            model_name='salesgroupsummarymodel',
            name='scompanyname',
        ),
        migrations.RemoveField(
            model_name='salesledger_m_summarymodel',
            name='sBranchsummary_frgn',
        ),
        migrations.RemoveField(
            model_name='salesledgervouchermodel',
            name='sledgersummary_frgn',
        ),
        migrations.DeleteModel(
            name='Bledgersummarypagemodel',
        ),
        migrations.DeleteModel(
            name='bledgervouchermodel',
        ),
        migrations.DeleteModel(
            name='Direct_GroupSummaryModel',
        ),
        migrations.DeleteModel(
            name='Direct_ledger_m_summarymodel',
        ),
        migrations.DeleteModel(
            name='Direct_ledgervouchermodel',
        ),
        migrations.DeleteModel(
            name='Purchase_ledger_m_summarymodel',
        ),
        migrations.DeleteModel(
            name='Purchase_ledgervouchermodel',
        ),
        migrations.DeleteModel(
            name='PurchaseGroupSummaryModel',
        ),
        migrations.DeleteModel(
            name='salesGroupSummaryModel',
        ),
        migrations.DeleteModel(
            name='salesledger_m_summarymodel',
        ),
        migrations.DeleteModel(
            name='salesledgervouchermodel',
        ),
    ]
