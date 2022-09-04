from django.contrib import admin
from app1.models import *
# Register your models here.

@admin.register(createcompanymodel)
class createcompany(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(BranchGroupSummaryModel)
class bgroupsummary(admin.ModelAdmin):
    list_display = ('id','companyname','bopeningbalace','bperticulars','bdebit','bcredit')

@admin.register(Bledgersummarypagemodel)
class bledgersummary(admin.ModelAdmin):
    list_display = ('id','Branchsummary_frgn','bperticulars','bdebit','bcredit','bclosingbalance')

@admin.register(bledgervouchermodel)
class bledgervoucher(admin.ModelAdmin):
    list_display = ('id','bledgersummary_frgn','bdate','bperticular','bvchtype','bvchno','bdebit','bcredit')

@admin.register(salesGroupSummaryModel)
class sgroupsummary(admin.ModelAdmin):
    list_display = ('id','scompanyname','sopeningbalace','sperticulars','sdebit','scredit')

@admin.register(salesledger_m_summarymodel)
class sledgermonthlysummary(admin.ModelAdmin):
    list_display = ('id','sBranchsummary_frgn','sperticulars','sdebit','scredit','sclosingbalance')