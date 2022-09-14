from importlib.resources import contents
from multiprocessing import context
from webbrowser import get
from django.shortcuts import render,redirect
from django.db.models import*
from app1.models import*


# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

# My Html Pages

def trialbalance(request):
    
    return render(request,'trial/trialbalance.html',)

def groupsummarypage(request):
    sdata=createcompanymodel.objects.all()
    data=BranchGroupSummaryModel.objects.all()
    sum1=0
    sum2=0
    for a in data:
        sum1+=a.bdebit
    for b in data:
        sum2+=b.bcredit
    context={'data':data,'sdata':sdata,'sum1':sum1,'sum2':sum2}
    return render(request,'trial/bgroupsummary.html',context)
   

def ledger_m_summary_page(request,pk):
    display=BranchGroupSummaryModel.objects.get(id=pk)
    data=Bledgersummarypagemodel.objects.filter(Branchsummary_frgn=display)
    sum1=0
    sum2=0
    sum3=0
    
    for i in data:
        sum1+=i.bdebit
    for i in data:
        sum2+=i.bcredit
    for i in data:
        sum3+=i.bclosingbalance 
    context={"data":data,'display':display,'sum1':sum1,'sum2':sum2,'sum3':sum3}
    return render(request,'trial/bledgermonthlysummary.html',context)
# def ledger_m_summary_page(request,pk):
#     data=Bledgersummarypagemodel.objects.get(id=pk)
#     sdata=BranchGroupSummaryModel.objects.filter(Branchsummary_frgn=data)
#     context={'sdata':sdata}
#     return render(request,'trial/bledgermonthlysummary.html',context)

def ledger_voucher_page(request,pk):
    data=Bledgersummarypagemodel.objects.get(id=pk)
    ndata=bledgervouchermodel.objects.filter(bledgersummary_frgn=data)
    sum1=0
    sum2=0
    for i in ndata:
        sum1+=i.bdebit
    for i in ndata:
        sum2+=i.bcredit
    cbalance=sum2-sum1
    context={'data':data,'ndata':ndata,'cbalance':cbalance,'sum1':sum1,'sum2':sum2}
    return render(request,'trial/bledgervoucher.html',context)

def sgroup_summary_page(request):
    ndata=createcompanymodel.objects.all()
    sdata=salesGroupSummaryModel.objects.all()
    sum1=0
    sum2=0
    for i in sdata:
        sum1+=i.sdebit
    for i in sdata:
        sum2+=i.scredit
    context={'ndata':ndata,'sdata':sdata,'sum1':sum1,'sum2':sum2}
    return render(request,'trial/sgroupsummary.html',context)

def sledger_m_summary_page(request,pk):
    adata=salesGroupSummaryModel.objects.get(id=pk)
    bdata=salesledger_m_summarymodel.objects.filter(sBranchsummary_frgn=adata)
    sum1=0
    sum2=0
    sum3=0
    for i in bdata:
        sum1+=i.sdebit
    for i in bdata:
        sum2+=i.scredit
    for i in bdata:
        sum3+=i.sclosingbalance
    context={'adata':adata,'bdata':bdata,'sum1':sum1,'sum2':sum2,'sum3':sum3}
    return render(request,'trial/sledgermonthlysummary.html',context)

def sledger_voucher(request,pk):
    data=salesledger_m_summarymodel.objects.get(id=pk)
    ndata=salesledgervouchermodel.objects.filter(sledgersummary_frgn=data)
    sum1=0
    sum2=0
    sum3=0
    for i in ndata:
        sum1+=i.sdebit
    for i in ndata:
        sum2+=i.scredit
    for i in ndata:
        sum3=i.sledgersummary_frgn.sBranchsummary_frgn.sopeningbalace
    cbalance=sum2-sum1
    context={'data':data,'ndata':ndata,'sum1':sum1,'sum2':sum2,'sum3':sum3,'cbalance':cbalance}
    return render(request,'trial/sledgervoucher.html',context)

def pgroup_summary(request):
    ndata=createcompanymodel.objects.all()
    bdata=PurchaseGroupSummaryModel.objects.all()
    sum1=0
    sum2=0
    for i in bdata:
        sum1+=i.pdebit
    for i in bdata:
        sum2+=i.pcredit
    context={'ndata':ndata,'bdata':bdata,'sum1':sum1,'sum2':sum2}
    return render(request,'trial/pgroupsummary.html',context)

def pledger_m_summary_page(request,pk):
    adata=PurchaseGroupSummaryModel.objects.get(id=pk)
    bdata=Purchase_ledger_m_summarymodel.objects.filter(pBranchsummary_frgn=adata)
    sum1=0
    sum2=0
    sum3=0
    for i in bdata:
        sum1+=i.pdebit
    for i in bdata:
        sum2+=i.pcredit
    for i in bdata:
        sum3+=i.pclosingbalance
    context={'adata':adata,'bdata':bdata,'sum1':sum1,'sum2':sum2,'sum3':sum3}
    return render(request,'trial/pledgermonthlysummary.html',context)

def pledger_voucher(request,pk):
    data=Purchase_ledger_m_summarymodel.objects.get(id=pk)
    ndata=Purchase_ledgervouchermodel.objects.filter(pledgersummary_frgn=data)
    sum1=0
    sum2=0
    sum3=0
    for i in ndata:
        sum1+=i.pdebit
    for i in ndata:
        sum2+=i.pcredit
    for i in ndata:
        sum3=i.pledgersummary_frgn.pBranchsummary_frgn.popeningbalace
    cbalance=sum2-(sum1+sum3)
    context={'data':data,'ndata':ndata,'sum1':sum1,'sum2':sum2,'sum3':sum3,'cbalance':cbalance}
    return render(request,'trial/pledgervoucher.html',context)

def dgroup_summary(request):
    ndata=createcompanymodel.objects.all()
    bdata=Direct_GroupSummaryModel.objects.all()
    sum1=0
    sum2=0
    for i in bdata:
        sum1+=i.ddebit
    for i in bdata:
        sum2+=i.dcredit
    context={'ndata':ndata,'bdata':bdata,'sum1':sum1,'sum2':sum2}
    return render(request,'trial/dgroupsummary.html',context)

def dledger_m_summary_page(request,pk):
    adata=Direct_GroupSummaryModel.objects.get(id=pk)
    bdata=Direct_ledger_m_summarymodel.objects.filter(dBranchsummary_frgn=adata)
    sum1=0
    sum2=0
    sum3=0
    for i in bdata:
        sum1+=i.ddebit
    for i in bdata:
        sum2+=i.dcredit
    for i in bdata:
        sum3+=i.dclosingbalance
    context={'adata':adata,'bdata':bdata,'sum1':sum1,'sum2':sum2,'sum3':sum3}
    return render(request,'trial/dledgermonthlysummary.html',context)

def dledger_voucher(request,pk):
    data=Direct_ledger_m_summarymodel.objects.get(id=pk)
    ndata=Direct_ledgervouchermodel.objects.filter(dledgersummary_frgn=data)
    sum1=0
    sum2=0
    sum3=0
    for i in ndata:
        sum1+=i.ddebit
    for i in ndata:
        sum2+=i.dcredit
    for i in ndata:
        sum3=i.dledgersummary_frgn.dBranchsummary_frgn.dopeningbalace
    cbalance=sum2-(sum1+sum3)
    context={'data':data,'ndata':ndata,'sum1':sum1,'sum2':sum2,'sum3':sum3,'cbalance':cbalance}
    return render(request,'trial/dledgervoucher.html',context)