from calendar import month_name
from datetime import date
from operator import mod
from django.db import models

# Create your models here.

class createcompanymodel(models.Model):
    name=models.CharField(max_length=250)

# class createMonthmodel(models.Model):
#     month_name=models.CharField(max_length=250)

class BranchGroupSummaryModel(models.Model):
    companyname=models.ForeignKey(createcompanymodel,on_delete=models.CASCADE)
    bopeningbalace=models.IntegerField(default=0)
    bperticulars=models.CharField(max_length=250)
    bdebit=models.IntegerField()
    bcredit=models.IntegerField()

class Bledgersummarypagemodel(models.Model):
    Branchsummary_frgn=models.ForeignKey(BranchGroupSummaryModel,on_delete=models.CASCADE)
    # Bmonthname=models.ForeignKey(createMonthmodel,on_delete=models.CASCADE)
    bperticulars=models.CharField(max_length=250)
    bdebit=models.IntegerField()
    bcredit=models.IntegerField()
    bclosingbalance=models.IntegerField()

class bledgervouchermodel(models.Model):
    bledgersummary_frgn=models.ForeignKey(Bledgersummarypagemodel,on_delete=models.CASCADE)
    bdate=models.DateField(auto_now_add=True)
    bperticular=models.CharField(max_length=250)
    bvchtype=models.CharField(max_length=250)
    bvchno=models.IntegerField()
    bdebit=models.IntegerField()
    bcredit=models.IntegerField()
    
class salesGroupSummaryModel(models.Model):
    scompanyname=models.ForeignKey(createcompanymodel,on_delete=models.CASCADE)
    sopeningbalace=models.IntegerField(default=0)
    sperticulars=models.CharField(max_length=250)
    sdebit=models.IntegerField()
    scredit=models.IntegerField()

class salesledger_m_summarymodel(models.Model):
    sBranchsummary_frgn=models.ForeignKey(salesGroupSummaryModel,on_delete=models.CASCADE)
    sperticulars=models.CharField(max_length=250)
    sdebit=models.IntegerField()
    scredit=models.IntegerField()
    sclosingbalance=models.IntegerField()

class salesledgervouchermodel(models.Model):
    sledgersummary_frgn=models.ForeignKey(salesledger_m_summarymodel,on_delete=models.CASCADE)
    sdate=models.DateField(auto_now_add=True)
    sperticular=models.CharField(max_length=250)
    svchtype=models.CharField(max_length=250)
    svchno=models.IntegerField()
    sdebit=models.IntegerField()
    scredit=models.IntegerField()

class PurchaseGroupSummaryModel(models.Model):
    pcompanyname=models.ForeignKey(createcompanymodel,on_delete=models.CASCADE)
    popeningbalace=models.IntegerField(default=0)
    pperticulars=models.CharField(max_length=250)
    pdebit=models.IntegerField()
    pcredit=models.IntegerField()

class Purchase_ledger_m_summarymodel(models.Model):
    pBranchsummary_frgn=models.ForeignKey(PurchaseGroupSummaryModel,on_delete=models.CASCADE)
    pperticulars=models.CharField(max_length=250)
    pdebit=models.IntegerField()
    pcredit=models.IntegerField()
    pclosingbalance=models.IntegerField()

class Purchase_ledgervouchermodel(models.Model):
    pledgersummary_frgn=models.ForeignKey(Purchase_ledger_m_summarymodel,on_delete=models.CASCADE)
    pdate=models.DateField(auto_now_add=True)
    pperticular=models.CharField(max_length=250)
    pvchtype=models.CharField(max_length=250)
    pvchno=models.IntegerField()
    pdebit=models.IntegerField()
    pcredit=models.IntegerField()


class Direct_GroupSummaryModel(models.Model):
    dcompanyname=models.ForeignKey(createcompanymodel,on_delete=models.CASCADE)
    dopeningbalace=models.IntegerField(default=0)
    dperticulars=models.CharField(max_length=250)
    ddebit=models.IntegerField()
    dcredit=models.IntegerField()

class Direct_ledger_m_summarymodel(models.Model):
    dBranchsummary_frgn=models.ForeignKey(Direct_GroupSummaryModel,on_delete=models.CASCADE)
    dperticulars=models.CharField(max_length=250)
    ddebit=models.IntegerField()
    dcredit=models.IntegerField()
    dclosingbalance=models.IntegerField()

class Direct_ledgervouchermodel(models.Model):
    dledgersummary_frgn=models.ForeignKey(Direct_ledger_m_summarymodel,on_delete=models.CASCADE)
    ddate=models.DateField(auto_now_add=True)
    dperticular=models.CharField(max_length=250)
    dvchtype=models.CharField(max_length=250)
    dvchno=models.IntegerField()
    ddebit=models.IntegerField()
    dcredit=models.IntegerField()


    