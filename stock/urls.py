from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.InventoryListView.as_view(), name='inventory_lists'),
    path('<int:Sr_no>/<Dsr_no>/<Voucher_no>/<Recipt_date>/',views.inventory_detail,name='inventory_detail'),
    path('search/', views.post_search, name='post_search'),

    
]