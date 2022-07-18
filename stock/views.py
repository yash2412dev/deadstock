import imp
from django.shortcuts import render
from numpy import rec
from .models import inventory
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector
from .forms import  SearchForm
def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = inventory.objects.annotate(
                search=SearchVector('rv_no','current_locaton'),
            ).filter(search=query)
    return render(request,
                  'blog/post/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})

# Cre ate your views here.
def inventory_lists(request):
    object_list = inventory.objects.all()
    paginator = Paginator(object_list, 5) # 3 posts in each page
    page = request.GET.get('page')
    try:
        Inventory = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        Inventory = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        Inventory = paginator.page(paginator.num_pages)
    return render(request,
                 'blog/post/list.html',
                 {'page': page,
                  'inventory': Inventory})


def inventory_detail(request):
     invo = get_object_or_404(inventory ,name = 'name',rv_no = 'rv_no')
     
     return render(request,
                  'blog/post/detail.html',
                  {'invo': invo})


def inventory_detail(request,Sr_no ,Dsr_no,Voucher_no,Recipt_date):
    post = get_object_or_404(inventory, Sr_no = Sr_no,Dsr_no=Dsr_no,Voucher_no=Voucher_no,Recipt_date= Recipt_date)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

class InventoryListView(ListView):
    queryset = inventory.objects.all()
    context_object_name = 'inventory'
    paginate_by = 5
    template_name = 'blog/post/list.html'