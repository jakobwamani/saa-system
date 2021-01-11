from django.shortcuts import render
from django.http import HttpResponse
from mis.forms import InStockForm,SearchForm
from mis.models import stock

def index(request):
    return render(request,'index.html',{})

def instocking(request):
    if request.method == 'POST':
        f = InStockForm(request.POST)
        if f.is_valid():
            new_data=f.save(commit=False)
            new_data.save()
            return HttpResponse("Thanks")
        else:
            f = InStockForm()
    else:
        f = InStockForm()
    
    return render(request, 'instock.html', {'f': f})

def selling(request):
   
    query = request.GET.copy()
    # query = request.POST.get('searched_product')
    product = query.get('searchproduct')
    print (product)
    search = stock.objects.filter(product_name=product)
    print(search)
    # query = None
    # if request.method == 'get':
    #     search = SearchForm(request.GET)
    #     # url = request.GET.get("searched_product")
    #     # print(url)
    #     if search.is_valid():
    #         query = stock.objects.filter(product_name=search)
    #     else:
    #         return HttpResponse("thanks")
    # else:
    #     search = SearchForm()

    return render(request,'selling.html',{'search':search})
    