from django.contrib import admin
from app1.models import *
# Register your models here.

@admin.register(createcompanymodel)
class createcompany(admin.ModelAdmin):
    list_display = ('id','name')

# @admin.register(createMonthmodel)
# class createmonth(admin.ModelAdmin):
#     list_display = ('id','month_name')

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

@admin.register(salesledgervouchermodel)
class sledgervoucher(admin.ModelAdmin):
    list_display = ('id','sledgersummary_frgn','sdate','sperticular','svchtype','svchno','sdebit','scredit')



@admin.register(PurchaseGroupSummaryModel)
class pgroupsummary(admin.ModelAdmin):
    list_display = ('id','pcompanyname','popeningbalace','pperticulars','pdebit','pcredit')

@admin.register(Purchase_ledger_m_summarymodel)
class pledgermonthlysummary(admin.ModelAdmin):
    list_display = ('id','pBranchsummary_frgn','pperticulars','pdebit','pcredit','pclosingbalance')

@admin.register(Purchase_ledgervouchermodel)
class pledgervoucher(admin.ModelAdmin):
    list_display = ('id','pledgersummary_frgn','pdate','pperticular','pvchtype','pvchno','pdebit','pcredit')




@admin.register(Direct_GroupSummaryModel)
class dgroupsummary(admin.ModelAdmin):
    list_display = ('id','dcompanyname','dopeningbalace','dperticulars','ddebit','dcredit')

@admin.register(Direct_ledger_m_summarymodel)
class dledgermonthlysummary(admin.ModelAdmin):
    list_display = ('id','dBranchsummary_frgn','dperticulars','ddebit','dcredit','dclosingbalance')

@admin.register(Direct_ledgervouchermodel)
class dledgervoucher(admin.ModelAdmin):
    list_display = ('id','dledgersummary_frgn','ddate','dperticular','dvchtype','dvchno','ddebit','dcredit')

