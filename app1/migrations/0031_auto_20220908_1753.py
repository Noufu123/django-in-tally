# Generated by Django 3.2.9 on 2022-09-08 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_auto_20220907_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesledgervouchermodel',
            name='sledgersummary_frgn',
        ),
        migrations.DeleteModel(
            name='salesledger_m_summarymodel',
        ),
        migrations.DeleteModel(
            name='salesledgervouchermodel',
        ),
    ]