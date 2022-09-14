from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),

    # My Html Pages

    path('trialbalance',views.trialbalance,name='trialbalance'),
    path('groupsummarypage',views.groupsummarypage,name='groupsummarypage'),
    path('ledger_m_summary_page/<int:pk>',views.ledger_m_summary_page,name='ledger_m_summary_page'),
    path('ledger_voucher_page/<int:pk>',views.ledger_voucher_page,name='ledger_voucher_page'),

    path('sgroup_summary_page',views.sgroup_summary_page,name='sgroup_summary_page'),
    path('sledger_m_summary_page/<int:pk>',views.sledger_m_summary_page,name='sledger_m_summary_page'),
    path('sledger_voucher/<int:pk>',views.sledger_voucher,name='sledger_voucher'),

    path('pgroup_summary',views.pgroup_summary,name='pgroup_summary'),
    path('pledger_m_summary_page/<int:pk>',views.pledger_m_summary_page,name='pledger_m_summary_page'),
    path('pledger_voucher/<int:pk>',views.pledger_voucher,name='pledger_voucher'),

    path('dgroup_summary',views.dgroup_summary,name='dgroup_summary'),
    path('dledger_m_summary_page/<int:pk>',views.dledger_m_summary_page,name='dledger_m_summary_page'),
    path('dledger_voucher/<int:pk>',views.dledger_voucher,name='dledger_voucher'),
    
]