from datetime import date
from operator import mod
from django.db import models

# Create your models here.

class createcompanymodel(models.Model):
    name=models.CharField(max_length=250)

class BranchGroupSummaryModel(models.Model):
    companyname=models.ForeignKey(createcompanymodel,on_delete=models.CASCADE)
    bopeningbalace=models.IntegerField(default=0)
    bperticulars=models.CharField(max_length=250)
    bdebit=models.IntegerField()
    bcredit=models.IntegerField()

class Bledgersummarypagemodel(models.Model):
    Branchsummary_frgn=models.ForeignKey(BranchGroupSummaryModel,on_delete=models.CASCADE)
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
